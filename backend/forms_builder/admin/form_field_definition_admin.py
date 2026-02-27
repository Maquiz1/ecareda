from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from ..models import FormDefinition, FormFieldDefinition, FormResponse, FieldValue

admin.site.register(FormFieldDefinition, SimpleHistoryAdmin)