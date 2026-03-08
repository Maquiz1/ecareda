from django.shortcuts import render


class OrganizationRequiredMiddleware:
    """
    Ensure logged-in users belong to an organization.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        user = request.user
        path = request.path

        # Allow these paths without organization
        allowed_paths = (
            "/accounts/",
            "/admin/",
            "/static/",
            "/media/",
        )

        if path.startswith(allowed_paths):
            return self.get_response(request)

        # Skip checks for anonymous users
        if user.is_authenticated:

            # Allow superusers
            if user.is_superuser:
                return self.get_response(request)

            # Block users without organization
            if not getattr(user, "organization", None):
                return render(
                    request,
                    "core/errors/no_organization.html",
                    status=403
                )

        return self.get_response(request)