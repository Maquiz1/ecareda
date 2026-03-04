from django.db import models
from core.tenant import get_current_user


class TenantQuerySet(models.QuerySet):

    def for_current_tenant(self):
        user = get_current_user()

        if user and hasattr(user, "organization") and user.organization:
            return self.filter(organization=user.organization)

        return self


class TenantManager(models.Manager):

    def get_queryset(self):

        qs = TenantQuerySet(self.model, using=self._db)

        user = get_current_user()

        # Superusers can see everything
        if user and user.is_superuser:
            return qs

        # Filter by organization
        if user and hasattr(user, "organization") and user.organization:
            qs = qs.filter(organization=user.organization)

        return qs
    
    
from django.db import models
from core.tenant import get_current_user


class TenantQuerySet(models.QuerySet):

    def for_current_tenant(self):
        user = get_current_user()

        if user and hasattr(user, "organization") and user.organization:
            return self.filter(organization=user.organization)

        return self




# Prevent AnonymousUser issues - THis Version i will test later

# class TenantManager(models.Manager):

#     def get_queryset(self):

#         qs = TenantQuerySet(self.model, using=self._db)

#         user = get_current_user()

#         # Superusers can see everything
#         if user and user.is_superuser:
#             return qs

#         # Filter by organization
#         if user and hasattr(user, "organization") and user.organization:
#             qs = qs.filter(organization=user.organization)

#         return qs