from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from ..models import Subject


@admin.register(Subject)
class SubjectAdmin(SimpleHistoryAdmin):
    list_display = (
        "subject_id",
        "project",
        "site",
        "organization",
        "enrollment_date",
    )

    search_fields = ("subject_id",)

    list_filter = (
        "organization",
        "project",
        "site",
        "site__country",
    )