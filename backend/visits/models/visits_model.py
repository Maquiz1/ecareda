from django.db import models
from simple_history.models import HistoricalRecords
from patients.models import Patient
from constants.visit_types_constants import VISIT_TYPES

class Visit(models.Model):

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_type = models.CharField(max_length=50, choices=VISIT_TYPES)
    visit_number = models.PositiveIntegerField()
    visit_date = models.DateField()
    notes = models.TextField(blank=True)

    history = HistoricalRecords()

    class Meta:
        unique_together = ("patient", "visit_number")
        ordering = ["visit_date"]


    def save(self, *args, **kwargs):
        is_new = self.pk is None
        super().save(*args, **kwargs)

        if is_new:
            from forms_builder.models import VisitTypeFormAssignment, FormResponse

            assignments = VisitTypeFormAssignment.objects.filter(
                project=self.patient.project,
                visit_type=self.visit_type
            )

            for assignment in assignments:
                FormResponse.objects.get_or_create(
                    visit=self,
                    form=assignment.form
                )

    def __str__(self):
        return f"{self.patient.subject_id} - Visit {self.visit_number}"