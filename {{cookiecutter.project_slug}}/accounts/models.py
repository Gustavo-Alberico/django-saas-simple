from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from accounts.mixins import BaseMixin, TenantMixin
from accounts.manager import TenantManager


class Tenant(TenantMixin):
    paid_until = models.DateField()
    on_trial = models.BooleanField()
    created_at = models.DateField(auto_now_add=True)
    created_by = models.OneToOneField(
        "User", on_delete=models.CASCADE, related_name="user_tenant"
    )


class TenantModel(BaseMixin):
    tenant = models.ForeignKey(
        Tenant, db_index=True, on_delete=models.CASCADE, null=True
    )

    tenant_objects = TenantManager()

    class Meta:
        abstract = True


class User(AbstractUser, TenantModel):
    pass
