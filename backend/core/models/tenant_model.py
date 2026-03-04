from django.db import models
from organizations.models import Organization
from core.managers.tenant_manager import TenantManager


class TenantModel(models.Model):

    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE
    )

    objects = TenantManager()

    class Meta:
        abstract = True