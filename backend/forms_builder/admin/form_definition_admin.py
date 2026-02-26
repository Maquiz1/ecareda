from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from ..models import FormDefinition, FormFieldDefinition, FormResponse, FieldValue


class FormFieldInline(admin.TabularInline):
    model = FormFieldDefinition
    extra = 1


@admin.register(FormDefinition)
class FormDefinitionAdmin(SimpleHistoryAdmin):
    list_display = ("name", "project", "is_active")
    inlines = [FormFieldInline]


admin.site.register(FormResponse, SimpleHistoryAdmin)
admin.site.register(FieldValue, SimpleHistoryAdmin)