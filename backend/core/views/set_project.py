from django.shortcuts import redirect
from projects.models import Project
from organizations.models import Organization


def set_project(request, project_id):

    project = Project.objects.get(id=project_id)

    request.session["project_id"] = project.id

    return redirect(request.META.get("HTTP_REFERER", "/"))