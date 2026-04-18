from projects.models import Project
from organizations.models import Organization


def current_context(request):

    project_id = request.session.get("project_id")
    org_id = request.session.get("org_id")

    current_project = None
    current_org = None

    if project_id:
        current_project = Project.objects.filter(id=project_id).first()

    if org_id:
        current_org = Organization.objects.filter(id=org_id).first()

    return {

        "current_project": current_project,
        "current_org": current_org,
        "user_projects": Project.objects.filter(organization_id=org_id) if org_id else Project.objects.all(),
        "user_orgs": Organization.objects.all(),
    }