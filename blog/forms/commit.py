from django import forms
from django.core.exceptions import ObjectDoesNotExist

from ..models.git_commit import GitCommit
from ..models.ticket import Ticket


class LinkCommitForm(forms.Form):
    commit = forms.ModelChoiceField(
        queryset=GitCommit.objects.none(),
        empty_label="— Select a commit —",
        label="Commit",
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    def __init__(self, ticket, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["commit"].queryset = self._build_unlinked_commit_queryset(ticket)

    def _build_unlinked_commit_queryset(self, ticket):
        try:
            git_repository = ticket.project.git_repository
        except ObjectDoesNotExist:
            return GitCommit.objects.none()
        already_linked_ids = ticket.commit_links.values_list("git_commit_id", flat=True)
        return (
            GitCommit.objects
            .filter(git_repository=git_repository)
            .exclude(id__in=already_linked_ids)
            .select_related("git_repository")
            .order_by("-commit_date")
        )
