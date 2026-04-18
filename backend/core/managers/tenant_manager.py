from django.db import models
from core.tenant.tenant import get_current_user, get_current_org


class TenantQuerySet(models.QuerySet):

    def for_current_tenant(self):
        org_id = get_current_org()
        if org_id:
            return self.filter(organization_id=org_id)
        
        user = get_current_user()
        if user and hasattr(user, "organization") and user.organization:
            return self.filter(organization=user.organization)

        return self


class TenantManager(models.Manager):

    def get_queryset(self):

        qs = TenantQuerySet(self.model, using=self._db)

        org_id = get_current_org()
        user = get_current_user()

        # Priority 1: Filter by explicitly set session organization (for all users)
        if org_id:
            return qs.filter(organization_id=org_id)

        # Priority 2: Fallback to user's assigned organization if not superuser
        if user and not user.is_superuser and hasattr(user, "organization") and user.organization:
            return qs.filter(organization=user.organization)

        # Superusers with no session org pick see everything
        return qs