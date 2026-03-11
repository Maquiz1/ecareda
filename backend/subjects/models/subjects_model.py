from django.db import models
from organizations.models import Organization
from sites.models import Site
from projects.models import Project
from simple_history.models import HistoricalRecords
from core.models import TenantAuditModel,ActiveModel


class Subject(TenantAuditModel,ActiveModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    subject_id = models.CharField(max_length=50)
    enrollment_date = models.DateField(null=True, blank=True)

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        # Check organization_id instead of organization
        if not self.organization_id and self.project:
            self.organization = self.project.organization
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.subject_id} ({self.project.name})"