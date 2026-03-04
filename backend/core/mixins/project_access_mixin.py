from django.core.exceptions import PermissionDenied


class ProjectAccessMixin:
    """
    Ensure project belongs to the user's organization.
    """

    def dispatch(self, request, *args, **kwargs):

        project = getattr(self.get_object(), "project", None)

        if project and project.organization != request.user.organization:
            raise PermissionDenied("You do not have access to this project.")

        return super().dispatch(request, *args, **kwargs)