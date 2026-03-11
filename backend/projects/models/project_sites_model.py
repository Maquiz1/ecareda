from django.db import models
from sites.models import Site
from . projects_model import Project
from core.models import TenantAuditModel,ActiveModel

class ProjectSite(TenantAuditModel,ActiveModel):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    code = models.CharField(max_length=50, unique=True)
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    # is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.project.name} - {self.site.name}"