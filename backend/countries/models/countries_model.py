from django.db import models
from organizations.models import Organization

class Country(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50, unique=True)
    iso_code = models.CharField(max_length=3)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.organization.name})"