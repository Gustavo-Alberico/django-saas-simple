from django.db import models

from accounts.utils import get_current_tenant


class TenantManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(tenant=get_current_tenant())
