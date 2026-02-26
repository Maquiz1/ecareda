from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from ..models import Site


@admin.register(Site)
class SiteAdmin(SimpleHistoryAdmin):
    list_display = ("name", "code", "country", "organization")
    search_fields = ("name", "code")
    list_filter = ("organization", "country")