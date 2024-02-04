import uuid
from django.db import models, transaction
from django.conf import settings


class BaseMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TenantMixin(BaseMixin):
    name = models.CharField(max_length=100)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name
