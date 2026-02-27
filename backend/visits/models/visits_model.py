from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords
from django.apps import apps

from patients.models import Patient
from constants.visit_types_constants import VISIT_TYPES


class Visit(models.Model):

    VISIT_STATUS = (
        ("open", "Open"),
        ("completed", "Completed"),
        ("verified", "Verified"),
        ("locked", "Locked"),
    )

    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE
    )

    visit_type = models.CharField(
        max_length=50,
        choices=VISIT_TYPES
    )

    visit_number = models.PositiveIntegerField()

    visit_date = models.DateField()

    notes = models.TextField(blank=True)

    status = models.CharField(
        max_length=20,
        choices=VISIT_STATUS,
        default="open"
    )

    # Visit-level locking
    locked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="locked_visits"
    )

    locked_at = models.DateTimeField(
        null=True,
        blank=True
    )

    history = HistoricalRecords()

    class Meta:
        unique_together = ("patient", "visit_number")
        ordering = ["visit_date"]

    def save(self, *args, **kwargs):
        is_new = self.pk is None

        # Prevent modification if visit is locked
        if self.pk:
            original = Visit.objects.get(pk=self.pk)
            if original.status == "locked":
                raise ValueError("Locked visits cannot be modified.")

        super().save(*args, **kwargs)

        # Auto-create required forms when visit is first created
        if is_new:
            VisitTypeFormAssignment = apps.get_model(
                "forms_builder", "VisitTypeFormAssignment"
            )
            FormResponse = apps.get_model(
                "forms_builder", "FormResponse"
            )

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