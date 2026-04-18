from projects.models import Project
from organizations.models import Organization
from countries.models.countries_model import Country
from sites.models import Site


def current_context(request):

    project_id = request.session.get("project_id")
    org_id = request.session.get("org_id")
    country_id = request.session.get("country_id")
    site_id = request.session.get("site_id")

    current_project = None
    current_org = None
    current_country = None
    current_site = None

    # Filter Organization
    if org_id:
        current_org = Organization.objects.filter(id=org_id).first()

    # Filter Country
    if country_id and org_id:
        current_country = Country.objects.filter(id=country_id, organization_id=org_id).first()

    # Filter Project
    if project_id and org_id:
        current_project = Project.objects.filter(id=project_id, organization_id=org_id).first()
        
    # Filter Site
    if site_id and org_id:
        site_qs = Site.objects.filter(id=site_id, organization_id=org_id)
        if country_id:
            site_qs = site_qs.filter(country_id=country_id)
        current_site = site_qs.first()

    return {
        "current_project": current_project,
        "current_org": current_org,
        "current_country": current_country,
        "current_site": current_site,
        
        "user_orgs": Organization.objects.all(),
        "user_countries": Country.objects.filter(organization_id=org_id) if org_id else Country.objects.none(),
        "user_projects": Project.objects.filter(organization_id=org_id) if org_id else Project.objects.none(),
        "user_sites": Site.objects.filter(organization_id=org_id) if org_id else Site.objects.none(),
    }