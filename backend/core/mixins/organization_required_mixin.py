from django.core.exceptions import PermissionDenied


class OrganizationRequiredMixin:
    """
    Ensure the logged-in user belongs to an organization.
    """

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, "organization") or request.user.organization is None:
            raise PermissionDenied("User is not assigned to an organization.")
        return super().dispatch(request, *args, **kwargs)