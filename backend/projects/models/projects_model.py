from django.db import models
from organizations.models import Organization
from sites.models import Site

class Project(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    protocol_number = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    sites = models.ManyToManyField(Site, through='ProjectSite')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
