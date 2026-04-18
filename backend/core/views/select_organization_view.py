from django.shortcuts import render, redirect
from organizations.models import Organization

def select_organization(request):
    """
    View to let users (especially superusers) pick an organization.
    """
    # For superusers, show all active organizations
    if request.user.is_superuser:
        organizations = Organization.objects.filter(is_active=True)
    # For regular users, show only their assigned organization(s)
    else:
        # Note: Current user model only has one organization FK, but we might want to support more later.
        user_org = getattr(request.user, 'organization', None)
        organizations = [user_org] if user_org else []
        
        # Fast-track if only one org exists
        if len(organizations) == 1:
            request.session["org_id"] = organizations[0].id
            return redirect("dashboard:dashboard")

    if request.method == "POST":
        org_id = request.POST.get("org_id")
        if org_id:
            request.session["org_id"] = org_id
            return redirect("dashboard:dashboard")

    context = {
        'organizations': organizations,
    }
    return render(request, "core/select_organization.html", context)
