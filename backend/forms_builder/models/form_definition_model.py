from django.db import models
from simple_history.models import HistoricalRecords
from projects.models import Project

class FormDefinition(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    history = HistoricalRecords()

    class Meta:
        unique_together = ("project", "name")

    def __str__(self):
        return f"{self.name} ({self.project.name})"

