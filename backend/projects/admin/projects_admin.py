from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from ..models import Project, ProjectSite


class ProjectSiteInline(admin.TabularInline):
    model = ProjectSite
    extra = 1


@admin.register(Project)
class ProjectAdmin(SimpleHistoryAdmin):
    list_display = ("name", "protocol_number", "organization", "start_date", "end_date")
    search_fields = ("name", "protocol_number")
    list_filter = ("organization", "start_date")
    inlines = [ProjectSiteInline]