import logging
from typing import Dict, List

from django.utils import timezone
from django.utils.dateparse import parse_datetime

from ..models.git_commit import GitCommit
from ..models.git_repository import GitRepository

logger = logging.getLogger(__name__)

COMMIT_FETCH_LIMIT = 100


class GitSyncService:
    """Syncs GitHub push payload commits into the local GitCommit store."""

    def __init__(self, git_repository: GitRepository):
        self.git_repository = git_repository

    def sync_commits_from_push_payload(self, commits_payload: List[Dict]) -> int:
        """
        Upsert commits from a GitHub push event payload.
        Returns the number of new commits created.
        """
        created_count = 0
        for commit_data in commits_payload[:COMMIT_FETCH_LIMIT]:
            was_created = self._upsert_commit(commit_data)
            if was_created:
                created_count += 1
        self._update_last_synced()
        return created_count

    def _upsert_commit(self, commit_data: Dict) -> bool:
        """Create commit if new, skip if already exists. Returns True if created."""
        sha = commit_data.get("id") or commit_data.get("sha", "")
        if not sha:
            logger.warning("Skipping commit with missing SHA in push payload.")
            return False

        _, created = GitCommit.objects.get_or_create(
            sha=sha,
            git_repository=self.git_repository,
            defaults={
                "message": commit_data.get("message", "")[:2000],
                "author_name": _extract_author_name(commit_data),
                "author_email": _extract_author_email(commit_data),
                "commit_date": _parse_commit_date(commit_data),
                "commit_url": commit_data.get("url", "")[:500],
            },
        )
        return created

    def _update_last_synced(self):
        GitRepository.objects.filter(pk=self.git_repository.pk).update(
            last_synced_at=timezone.now()
        )


def _extract_author_name(commit_data: Dict) -> str:
    author = commit_data.get("author", {})
    return author.get("name", "Unknown")[:200]


def _extract_author_email(commit_data: Dict) -> str:
    author = commit_data.get("author", {})
    return author.get("email", "")[:254]


def _parse_commit_date(commit_data: Dict):
    raw = commit_data.get("timestamp", "")
    parsed = parse_datetime(raw) if raw else None
    return parsed or timezone.now()
