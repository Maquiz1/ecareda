from django.db import models
from simple_history.models import HistoricalRecords
from constants.visit_types_constants import VISIT_TYPES
from forms_builder.models import FormDefinition


class VisitTypeFormAssignment(models.Model):

    project = models.ForeignKey(
        "projects.Project",
        on_delete=models.CASCADE,
        related_name="visit_form_assignments"
    )

    visit_type = models.CharField(
        max_length=50,
        choices=VISIT_TYPES
    )

    form = models.ForeignKey(
        FormDefinition,
        on_delete=models.CASCADE,
        related_name="visit_assignments"
    )

    is_required = models.BooleanField(default=True)

    history = HistoricalRecords()

    class Meta:
        unique_together = ("project", "visit_type", "form")

    def __str__(self):
        return f"{self.project.name} | {self.visit_type} | {self.form.name}"