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

        if path.startswith(allowed_paths) or path == "/core/select-organization/":
            return self.get_response(request)

        # Skip checks for anonymous users
        if user.is_authenticated:
            # Check for current organization in session
            org_id = request.session.get('org_id')
            
            if not org_id:
                # 1. Try to auto-assign if the user has a primary organization in their profile
                user_org = getattr(user, "organization", None)
                if user_org:
                    request.session['org_id'] = user_org.id
                elif user.is_superuser:
                    # 2. If superuser with no org, redirect to selection page
                    from django.shortcuts import redirect
                    return redirect("core:select_organization")
                else:
                    # 3. Regular user with no org assigned at all -> Block
                    return render(
                        request,
                        "core/errors/no_organization.html",
                        status=403
                    )

        return self.get_response(request)