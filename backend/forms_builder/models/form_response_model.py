from django.db import models
from django.conf import settings
from simple_history.models import HistoricalRecords
from django.apps import apps

from .form_definition_model import FormDefinition


class FormResponse(models.Model):

    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("completed", "Completed"),
        ("reviewed", "Reviewed"),
        ("verified", "Verified"),
        ("signed", "Signed"),
        ("locked", "Locked"),
    )

    visit = models.ForeignKey(
        "visits.Visit",   # string reference to avoid circular import
        on_delete=models.CASCADE
    )

    form = models.ForeignKey(
        FormDefinition,
        on_delete=models.CASCADE
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="draft"
    )

    submitted_at = models.DateTimeField(auto_now_add=True)

    # Electronic Signature
    signed_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="signed_forms"
    )

    signed_at = models.DateTimeField(null=True, blank=True)

    signature_meaning = models.CharField(
        max_length=255,
        blank=True,
        help_text="Meaning of the signature (e.g., PI Approval)"
    )

    # Locking
    locked_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="locked_forms"
    )

    locked_at = models.DateTimeField(null=True, blank=True)

    history = HistoricalRecords()

    class Meta:
        unique_together = ("visit", "form")

    def save(self, *args, **kwargs):
        # Prevent modification if locked
        if self.pk:
            original = FormResponse.objects.get(pk=self.pk)
            if original.status == "locked":
                raise ValueError("Locked forms cannot be modified.")

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.form.name} - {self.visit}"