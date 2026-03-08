from django.db import models
from simple_history.models import HistoricalRecords
from . form_field_definition_model import FormFieldDefinition
from . form_response_model import FormResponse

class FieldValue(models.Model):
    form_response = models.ForeignKey(
        FormResponse,
        on_delete=models.CASCADE,
        related_name="field_values"
    )
    field = models.ForeignKey(FormFieldDefinition, on_delete=models.CASCADE,related_name="values")
    value = models.TextField(blank=True)

    history = HistoricalRecords()

    class Meta:
        unique_together = ("form_response", "field")

    def __str__(self):
        return f"{self.field.label} = {self.value}"