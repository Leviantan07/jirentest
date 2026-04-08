import hashlib
import hmac
import json
import logging

from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ..models import GitCommit, GitRepository, Project, Ticket, TicketCommitLink
from ..services.git_sync_service import GitSyncService
from .permissions import has_project_access

logger = logging.getLogger(__name__)

GITHUB_SIGNATURE_HEADER = "HTTP_X_HUB_SIGNATURE_256"
SHA256_PREFIX = "sha256="


def _is_valid_github_signature(request_body: bytes, signature_header: str) -> bool:
    """Validate HMAC SHA256 signature from GitHub webhook."""
    webhook_secret = getattr(settings, "GITHUB_WEBHOOK_SECRET", "")
    if not webhook_secret:
        logger.warning("GITHUB_WEBHOOK_SECRET not configured — skipping signature check.")
        return True
    if not signature_header or not signature_header.startswith(SHA256_PREFIX):
        return False
    expected = hmac.new(
        webhook_secret.encode(),
        request_body,
        hashlib.sha256,
    ).hexdigest()
    received = signature_header[len(SHA256_PREFIX):]
    return hmac.compare_digest(expected, received)


def _get_project_and_ticket(request, project_pk, ticket_pk):
    """Return (project, ticket, None) or (None, None, error_response)."""
    try:
        project = Project.objects.select_related("git_repository").get(pk=project_pk)
    except Project.DoesNotExist:
        return None, None, Response(
            {"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND
        )
    if not has_project_access(request.user, project):
        return None, None, Response(
            {"error": "Permission denied."}, status=status.HTTP_403_FORBIDDEN
        )
    try:
        ticket = Ticket.objects.get(pk=ticket_pk, project=project)
    except Ticket.DoesNotExist:
        return None, None, Response(
            {"error": "Ticket not found"}, status=status.HTTP_404_NOT_FOUND
        )
    return project, ticket, None


@csrf_exempt
@api_view(["POST"])
@permission_classes([])
def github_webhook_receiver(request):
    """
    Receives GitHub push webhook events and syncs commits into the local DB.
    Uses HMAC SHA256 signature validation — no authentication required.
    """
    signature = request.META.get(GITHUB_SIGNATURE_HEADER, "")
    if not _is_valid_github_signature(request.body, signature):
        logger.warning("Rejected GitHub webhook: invalid HMAC signature.")
        return Response({"error": "Invalid signature"}, status=status.HTTP_403_FORBIDDEN)

    try:
        payload = json.loads(request.body)
    except json.JSONDecodeError:
        return Response({"error": "Invalid JSON payload"}, status=status.HTTP_400_BAD_REQUEST)

    repo_url = payload.get("repository", {}).get("html_url", "")
    commits_data = payload.get("commits", [])

    if not repo_url or not commits_data:
        return Response({"status": "no_commits"}, status=status.HTTP_200_OK)

    try:
        git_repository = GitRepository.objects.get(repository_url=repo_url)
    except GitRepository.DoesNotExist:
        logger.info("Webhook received for unregistered repository: %s", repo_url)
        return Response({"status": "repository_not_registered"}, status=status.HTTP_200_OK)

    try:
        sync_service = GitSyncService(git_repository)
        created_count = sync_service.sync_commits_from_push_payload(commits_data)
        return Response(
            {"status": "synced", "new_commits": created_count},
            status=status.HTTP_200_OK,
        )
    except Exception as error:
        logger.error("Webhook sync failed for %s: %s", repo_url, error)
        return Response({"status": "sync_failed"}, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def available_commits_for_ticket(request, project_pk, ticket_pk):
    """List commits from the project repo not yet linked to this ticket."""
    project, ticket, error = _get_project_and_ticket(request, project_pk, ticket_pk)
    if error:
        return error

    if not hasattr(project, "git_repository"):
        return Response([], status=status.HTTP_200_OK)

    already_linked_ids = TicketCommitLink.objects.filter(ticket=ticket).values_list(
        "git_commit_id", flat=True
    )
    commits = (
        GitCommit.objects
        .filter(git_repository=project.git_repository)
        .exclude(id__in=already_linked_ids)
        .select_related("git_repository")
        .order_by("-commit_date")[:50]
    )
    return Response(
        [
            {
                "id": c.id,
                "sha_short": c.sha_short,
                "message": c.message[:120],
                "author": c.author_name,
                "date": c.commit_date.isoformat(),
                "url": c.commit_url,
            }
            for c in commits
        ],
        status=status.HTTP_200_OK,
    )


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def link_commit_to_ticket(request, project_pk, ticket_pk):
    """Link a commit to a done ticket."""
    project, ticket, error = _get_project_and_ticket(request, project_pk, ticket_pk)
    if error:
        return error

    if ticket.status != Ticket.STATUS_DONE:
        return Response(
            {"error": "Commits can only be linked to tickets with status 'Done'."},
            status=status.HTTP_400_BAD_REQUEST,
        )

    commit_id = request.data.get("commit_id")
    if not commit_id:
        return Response({"error": "commit_id is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        git_commit = GitCommit.objects.select_related("git_repository").get(
            id=commit_id,
            git_repository=project.git_repository,
        )
    except GitCommit.DoesNotExist:
        return Response(
            {"error": "Commit not found in this project's repository."},
            status=status.HTTP_404_NOT_FOUND,
        )

    link, created = TicketCommitLink.objects.get_or_create(
        ticket=ticket,
        git_commit=git_commit,
        defaults={"linked_by": request.user},
    )
    if not created:
        return Response(
            {"error": "Commit already linked to this ticket."},
            status=status.HTTP_409_CONFLICT,
        )
    return Response(
        {"commit_id": git_commit.id, "linked_at": link.linked_at.isoformat()},
        status=status.HTTP_201_CREATED,
    )
