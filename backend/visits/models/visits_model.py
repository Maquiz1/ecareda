from django.db import models
from simple_history.models import HistoricalRecords
from patients.models import Patient


class Visit(models.Model):

    VISIT_TYPES = (
        ("screening", "Screening"),
        ("baseline", "Baseline"),
        ("followup", "Follow-up"),
        ("unscheduled", "Unscheduled"),
    )

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    visit_type = models.CharField(max_length=50, choices=VISIT_TYPES)
    visit_number = models.PositiveIntegerField()
    visit_date = models.DateField()
    notes = models.TextField(blank=True)

    history = HistoricalRecords()

    class Meta:
        unique_together = ("patient", "visit_number")
        ordering = ["visit_date"]

    def __str__(self):
        return f"{self.patient.subject_id} - Visit {self.visit_number}"