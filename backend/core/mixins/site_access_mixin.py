from django.core.exceptions import PermissionDenied


class SiteAccessMixin:
    """
    Ensure the site belongs to the user's organization.
    """

    def dispatch(self, request, *args, **kwargs):

        site = getattr(self.get_object(), "site", None)

        if site and site.organization != request.user.organization:
            raise PermissionDenied("You do not have access to this site.")

        return super().dispatch(request, *args, **kwargs)