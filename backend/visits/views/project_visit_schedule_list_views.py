from django.shortcuts import render, get_object_or_404
from projects.models import Project
from visits.models import ProjectVisitSchedule


def project_visit_schedule_list(request, project_id):

    project = get_object_or_404(Project, id=project_id)

    schedules = ProjectVisitSchedule.objects.filter(
        project=project
    ).order_by("visit_number")

    context = {
        "project": project,
        "schedules": schedules,
    }

    return render(
        request,
        "visits/project_visit_schedule_list.html",
        context
    )