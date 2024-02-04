from django.conf import settings


if getattr(settings, "TENANT_USE_ASGIREF", False):
    # asgiref must be installed, its included with Django >= 3.0
    from asgiref.local import Local as local
else:
    from threading import local

_thread_locals = _context = local()


def get_current_tenant():
    """
    Utils to get the tenant that hass been set in the current thread/context using `set_current_tenant`.
    Can be used by doing:
    ```
        my_class_object = get_current_tenant()
    ```
    Will return None if the tenant is not set
    """
    return getattr(_context, "tenant", None)


def set_current_tenant(tenant):
    """
    Utils to set a tenant in the current thread/context.
    Often used in a middleware once a user is logged in to make sure all db
    calls are sharded to the current tenant.
    Can be used by doing:
    ```
        get_current_tenant(tenant)
    ```
    """
    setattr(_context, "tenant", tenant)


def clean_local_thread():
    unset_current_tenant()


def unset_current_tenant():
    setattr(_context, "tenant", None)


def get_tenant_from_request(request) -> int:
    return request.user.tenant
