from django.db import models
from core.models.active_model import ActiveModel
from core.models.audit_model import AuditModel

class Organization(AuditModel, ActiveModel):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name