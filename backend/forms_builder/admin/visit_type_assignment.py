from django.contrib import admin
from ..models import VisitTypeFormAssignment

@admin.register(VisitTypeFormAssignment)
class VisitTypeFormAssignmentAdmin(admin.ModelAdmin):
    list_display = ("project", "visit_type", "form", "is_required")
    list_filter = ("project", "visit_type")