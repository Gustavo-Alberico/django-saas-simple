import os
import sys
import django
from django.db import transaction
from decouple import config

project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_path)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")
django.setup()

from accounts.models import Tenant, User


def create_initial_tenant(tenant_name, username, email, password):
    with transaction.atomic():
        try:
            tenant = Tenant(
                name=tenant_name,
                paid_until="2016-12-05",
                on_trial=False,
            )

            user = User.objects.create_superuser(
                username, email, password, tenant=tenant
            )
            tenant.created_by = user
            tenant.save()
        except Exception:
            transaction.set_rollback(True)


create_initial_tenant(
    tenant_name=config("ADMIN_TENANT_NAME"),
    username=config("ADMIN_USERNAME"),
    email=config("ADMIN_EMAIL"),
    password=config("ADMIN_PASSWORD"),
)
