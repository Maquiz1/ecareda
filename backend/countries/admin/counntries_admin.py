from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from ..models import Country


@admin.register(Country)
class CountryAdmin(SimpleHistoryAdmin):
    list_display = ("name", "iso_code", "organization")
    search_fields = ("name", "iso_code")
    list_filter = ("organization",)