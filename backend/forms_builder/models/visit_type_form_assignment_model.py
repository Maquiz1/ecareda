from django.db import models
from . form_definition_model import FormDefinition
from simple_history.models import HistoricalRecords
from constants.visit_types_constants import VISIT_TYPES

class VisitTypeFormAssignment(models.Model):
    project = models.ForeignKey("projects.Project", on_delete=models.CASCADE)
    visit_type = models.CharField(max_length=50, choices=VISIT_TYPES)
    form = models.ForeignKey(FormDefinition, on_delete=models.CASCADE)

    is_required = models.BooleanField(default=True)
    
    history = HistoricalRecords()


    def __str__(self):
        return f"{self.visit_type} - {self.form.name}"