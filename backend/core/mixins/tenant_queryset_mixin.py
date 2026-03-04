class TenantQuerysetMixin:
    """
    Restrict queryset to the user's organization and exclude soft-deleted records.
    """

    def get_queryset(self):
        qs = super().get_queryset()

        if hasattr(self.request.user, "organization"):
            qs = qs.filter(
                organization=self.request.user.organization,
                is_deleted=False
            )

        return qs