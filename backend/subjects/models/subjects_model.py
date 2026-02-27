from django.db import models
from organizations.models import Organization
from sites.models import Site
from projects.models import Project
from simple_history.models import HistoricalRecords
from core.models import TenantAuditModel


class Subject(TenantAuditModel):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    subject_id = models.CharField(max_length=50)
    enrollment_date = models.DateField(null=True,blank=True)

    history = HistoricalRecords()  # ✅ this enables audit trail

    def save(self, *args, **kwargs):
        if not self.organization:
            self.organization = self.project.organization
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.subject_id} ({self.project.name})"