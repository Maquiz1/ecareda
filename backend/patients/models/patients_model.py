from django.db import models
from organizations.models import Organization
from sites.models import Site
from projects.models import Project
from simple_history.models import HistoricalRecords

class Patient(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    subject_id = models.CharField(max_length=50)
    enrollment_date = models.DateField()

    history = HistoricalRecords()  # ✅ this enables audit trail

    def __str__(self):
        return f"{self.subject_id} ({self.project.name})"