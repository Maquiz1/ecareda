from django.db import models
from core.models import ActiveModel
from branches.models import Branch
from core.models import TenantAuditModel

class Center(TenantAuditModel,ActiveModel):
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE,related_name="branch_center")
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    # is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name