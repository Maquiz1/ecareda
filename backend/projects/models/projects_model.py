from django.db import models
from organizations.models import Organization
from sites.models import Site
from django.conf import settings

ARCHIVE_STATUS = (
    ("active", "Active"),
    ("locked", "Database Locked"),
    ("archived", "Archived"),
)

class Project(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    protocol_number = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    sites = models.ManyToManyField(Site, through='ProjectSite')
    is_active = models.BooleanField(default=True)
    
    
    archive_status = models.CharField(
        max_length=20,
        choices=ARCHIVE_STATUS,
        default="active"
    )

    archived_at = models.DateTimeField(null=True, blank=True)
    archived_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="archived_projects"
    )


    def __str__(self):
        return self.name
