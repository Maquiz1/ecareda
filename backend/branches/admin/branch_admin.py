from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from ..models import Branch


@admin.register(Branch)
class BranchAdmin(SimpleHistoryAdmin):
    list_display = ("name", "code", "is_active")
    search_fields = ("name", "code")
    list_filter = ("is_active",)