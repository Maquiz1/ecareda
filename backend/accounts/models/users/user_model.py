# accounts/models/users/user_model.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from organizations.models import Organization
from sites.models import Site


class User(AbstractUser):

    organization = models.ForeignKey(
        Organization,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    site = models.ForeignKey(
        Site,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    # EDC roles
    is_data_manager = models.BooleanField(default=False)
    is_monitor = models.BooleanField(default=False)
    is_pi = models.BooleanField(default=False)
    is_coordinator = models.BooleanField(default=False)

    def __str__(self):
        return self.username