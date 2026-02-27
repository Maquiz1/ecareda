from . tenant_model import TenantModel
from . audit_model import AuditModel
from . soft_delete_model import SoftDeleteModel


class TenantAuditModel(TenantModel, AuditModel,SoftDeleteModel):
    class Meta:
        abstract = True