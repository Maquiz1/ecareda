from django.contrib import admin
from visits.models import ProjectVisitSchedule


@admin.register(ProjectVisitSchedule)
class ProjectVisitScheduleAdmin(admin.ModelAdmin):

    list_display = (
        "project",
        "visit_number",
        "visit_type",
        "days_from_baseline",
        "window_before",
        "window_after",
        "is_required",
        "is_unscheduled",
    )

    list_filter = (
        "project",
        "visit_type",
        "is_required",
        "is_unscheduled",
    )

    search_fields = (
        "project__name",
    )

    ordering = (
        "project",
        "visit_number",
    )

    list_editable = (
        "visit_type",
        "days_from_baseline",
        "window_before",
        "window_after",
        "is_required",
    )