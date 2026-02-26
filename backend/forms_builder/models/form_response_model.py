from django.db import models
from simple_history.models import HistoricalRecords
from . form_definition_model import FormDefinition
from visits.models import Visit

class FormResponse(models.Model):
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    form = models.ForeignKey(FormDefinition, on_delete=models.CASCADE)
    submitted_at = models.DateTimeField(auto_now_add=True)
    is_locked = models.BooleanField(default=False)

    history = HistoricalRecords()

    class Meta:
        unique_together = ("visit", "form")

    def __str__(self):
        return f"{self.form.name} - {self.visit}"

