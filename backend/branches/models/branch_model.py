from django.db import models
from core.models import ActiveModel
from organizations.models import Organization
from core.models import TenantAuditModel

class Branch(TenantAuditModel,ActiveModel):
    organization = models.ForeignKey(Organization,on_delete=models.CASCADE,related_name="organization_branch")
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    # is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name="Branch"
        verbose_name_plural="Branches"
        
    def __str__(self):
        return self.name