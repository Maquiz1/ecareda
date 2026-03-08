from django.db import models
from projects.models import Project
from constants.visit_types_constants import VISIT_TYPES


class ProjectVisitSchedule(models.Model):

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name="visit_schedule"
    )

    visit_type = models.CharField(
        max_length=50,
        choices=VISIT_TYPES
    )

    visit_number = models.PositiveIntegerField()

    days_from_baseline = models.IntegerField()

    window_before = models.IntegerField(default=0)

    window_after = models.IntegerField(default=0)

    is_required = models.BooleanField(default=True)
    
    
    scheduled_date = models.DateField(null=True, blank=True)

    window_start = models.DateField(null=True, blank=True)

    window_end = models.DateField(null=True, blank=True)

    is_unscheduled = models.BooleanField(default=False)

    class Meta:
        ordering = ["visit_number"]
        unique_together = ("project", "visit_number")

    def __str__(self):
        return f"{self.project.name} - Visit {self.visit_number} ({self.visit_type})"