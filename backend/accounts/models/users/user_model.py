from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    organization = models.ForeignKey(
        "organizations.Organization",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    site = models.ForeignKey(
        "sites.Site",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    is_data_manager = models.BooleanField(default=False)
    is_monitor = models.BooleanField(default=False)
    is_pi = models.BooleanField(default=False)
    is_coordinator = models.BooleanField(default=False)

    def __str__(self):
        return self.username