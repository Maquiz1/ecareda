from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from ..models import ProjectSite

@admin.register(ProjectSite)
class ProjectSiteAdmin(SimpleHistoryAdmin):
    list_display = ("project", "code", "site")
    search_fields = ("project", "site")
    # list_filter = ("code")
