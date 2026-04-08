from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_GET, require_POST

from ..forms.commit import LinkCommitForm
from ..models import GitCommit, Project, Ticket, TicketCommitLink
from .permissions import is_project_member


def _get_project_and_ticket_for_member(user, project_pk, ticket_pk):
    """Return (project, ticket) or raise Http404 / PermissionDenied."""
    project = get_object_or_404(
        Project.objects.select_related("git_repository"),
        pk=project_pk,
    )
    if not is_project_member(user, project):
        raise PermissionDenied()
    ticket = get_object_or_404(Ticket, pk=ticket_pk, project=project)
    return project, ticket


@login_required
@require_GET
def ticket_commit_select_view(request, project_pk, ticket_pk):
    """Display dropdown of unlinked commits for a done ticket."""
    project, ticket = _get_project_and_ticket_for_member(
        request.user, project_pk, ticket_pk
    )
    form = LinkCommitForm(ticket=ticket)
    return render(
        request,
        "blog/ticket_commit_select.html",
        {"ticket": ticket, "project": project, "form": form},
    )


@login_required
@require_POST
def ticket_link_commit_view(request, project_pk, ticket_pk):
    """Link a selected commit to a done ticket."""
    project, ticket = _get_project_and_ticket_for_member(
        request.user, project_pk, ticket_pk
    )
    if ticket.status != Ticket.STATUS_DONE:
        raise PermissionDenied("Commits can only be linked to done tickets.")

    form = LinkCommitForm(ticket=ticket, data=request.POST)
    if not form.is_valid():
        return render(
            request,
            "blog/ticket_commit_select.html",
            {"ticket": ticket, "project": project, "form": form},
        )

    git_commit = form.cleaned_data["commit"]
    _, created = TicketCommitLink.objects.get_or_create(
        ticket=ticket,
        git_commit=git_commit,
        defaults={"linked_by": request.user},
    )
    if created:
        messages.success(request, f"Commit {git_commit.sha_short} linked to ticket.")
    else:
        messages.info(request, "This commit was already linked to the ticket.")

    return redirect("ticket-commits-list", project_pk=project.pk, ticket_pk=ticket.pk)


@login_required
@require_GET
def ticket_commit_list_view(request, project_pk, ticket_pk):
    """Display all commits linked to a ticket."""
    project, ticket = _get_project_and_ticket_for_member(
        request.user, project_pk, ticket_pk
    )
    commit_links = (
        TicketCommitLink.objects
        .filter(ticket=ticket)
        .select_related("git_commit__git_repository", "linked_by")
        .order_by("-git_commit__commit_date")
    )
    return render(
        request,
        "blog/ticket_commit_list.html",
        {
            "ticket": ticket,
            "project": project,
            "commit_links": commit_links,
            "can_link_commits": ticket.status == Ticket.STATUS_DONE,
        },
    )
