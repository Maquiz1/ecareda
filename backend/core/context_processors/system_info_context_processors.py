from django.conf import settings

def system_info(request):
    return {
        "system_version": settings.SYSTEM_VERSION,
        "organization_code": settings.ORGANIZATION_CODE,
        "project_code": settings.PROJECT_CODE,
    }