from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from visits.models import Visit
from forms_builder.models import FormResponse


class FormResponseInline(admin.TabularInline):
    model = FormResponse
    extra = 0


@admin.register(Visit)
class VisitAdmin(SimpleHistoryAdmin):
    list_display = ("patient", "visit_number", "visit_type", "visit_date")
    list_filter = ("visit_type", "visit_date")
    inlines = [FormResponseInline]
    