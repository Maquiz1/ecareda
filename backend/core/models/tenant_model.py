from django.db import models


class TenantModel(models.Model):
    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.CASCADE
    )

    class Meta:
        abstract = True