from django.db import models
from simple_history.models import HistoricalRecords
from . form_definition_model import FormDefinition
from django.conf import settings

class FormFieldDefinition(models.Model):

    FIELD_TYPES = (
        ("text", "Text"),
        ("number", "Number"),
        ("date", "Date"),
        ("boolean", "Yes/No"),
        ("select", "Dropdown"),
    )

    form = models.ForeignKey(FormDefinition, on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
    field_type = models.CharField(max_length=20, choices=FIELD_TYPES)
    required = models.BooleanField(default=False)
    order = models.PositiveIntegerField(default=0)
    choices = models.TextField(blank=True)

    history = HistoricalRecords()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.label} ({self.form.name})"
