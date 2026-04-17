from django.db import models
from core.managers.tenant_manager import TenantManager
from core.tenant import get_current_user


class TenantModel(models.Model):

    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE
    )

    objects = TenantManager()

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):

        user = get_current_user()

        # automatically assign organization
        if not self.organization_id and user and hasattr(user, "organization"):
            self.organization = user.organization

        super().save(*args, **kwargs)