from django.db import models
from organizations.models import Organization
from countries.models import Country
from core.models import TenantAuditModel

class Site(TenantAuditModel):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} ({self.country.name})"