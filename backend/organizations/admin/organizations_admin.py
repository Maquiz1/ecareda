from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from ..models import Organization


@admin.register(Organization)
class OrganizationAdmin(SimpleHistoryAdmin):
    list_display = ("name", "code", "is_active")
    search_fields = ("name", "code")
    list_filter = ("is_active",)