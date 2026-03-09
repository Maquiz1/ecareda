from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from ..models import Project, ProjectSite
from visits.models import ProjectVisitSchedule


class ProjectSiteInline(admin.TabularInline):
    model = ProjectSite
    extra = 1


class ProjectVisitScheduleInline(admin.TabularInline):
    model = ProjectVisitSchedule
    extra = 1
    ordering = ("visit_number",)
    fields = (
        "visit_number",
        "visit_type",
        "days_from_baseline",
        "window_before",
        "window_after",
        "is_required",
    )


@admin.register(Project)
class ProjectAdmin(SimpleHistoryAdmin):

    list_display = (
        "name",
        "protocol_number",
        "organization",
        "start_date",
        "end_date",
    )

    search_fields = (
        "name",
        "protocol_number",
    )

    list_filter = (
        "organization",
        "start_date",
    )

    inlines = [
        ProjectSiteInline,
        ProjectVisitScheduleInline
    ]