from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone

from .git_repository import GitRepository
from .ticket import Ticket

SHA_DISPLAY_LENGTH = 7


class GitCommit(models.Model):
    sha = models.CharField(max_length=40)
    message = models.TextField()
    author_name = models.CharField(max_length=200)
    author_email = models.EmailField()
    commit_date = models.DateTimeField()
    commit_url = models.URLField(max_length=500, blank=True)
    git_repository = models.ForeignKey(
        GitRepository,
        on_delete=models.CASCADE,
        related_name="commits",
    )
    synced_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-commit_date"]
        unique_together = [("sha", "git_repository")]
        indexes = [
            models.Index(fields=["git_repository", "-commit_date"]),
        ]
        verbose_name = "Git Commit"
        verbose_name_plural = "Git Commits"

    def __str__(self):
        return f"{self.sha_short} — {self.message[:60]}"

    @property
    def sha_short(self):
        return self.sha[:SHA_DISPLAY_LENGTH]


class TicketCommitLink(models.Model):
    ticket = models.ForeignKey(
        Ticket,
        on_delete=models.CASCADE,
        related_name="commit_links",
    )
    git_commit = models.ForeignKey(
        GitCommit,
        on_delete=models.CASCADE,
        related_name="ticket_links",
    )
    linked_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="commit_links",
    )
    linked_at = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = [("ticket", "git_commit")]
        ordering = ["-linked_at"]
        verbose_name = "Ticket Commit Link"
        verbose_name_plural = "Ticket Commit Links"

    def __str__(self):
        return f"Ticket #{self.ticket_id} ← {self.git_commit.sha_short}"

    def clean(self):
        if self.ticket.status != Ticket.STATUS_DONE:
            raise ValidationError(
                "Commits can only be linked to tickets with status 'Done'."
            )
