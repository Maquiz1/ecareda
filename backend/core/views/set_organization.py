from django.shortcuts import redirect
from projects.models import Project
from organizations.models import Organization

def set_organization(request, org_id):

    request.session["org_id"] = org_id

    return redirect(request.META.get("HTTP_REFERER", "/"))