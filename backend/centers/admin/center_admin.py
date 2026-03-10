from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from ..models import Center

@admin.register(Center)
class CenterAdmin(SimpleHistoryAdmin):
    list_display = ("name", "code", "is_active")
    search_fields = ("name", "code")
    list_filter = ("is_active",)