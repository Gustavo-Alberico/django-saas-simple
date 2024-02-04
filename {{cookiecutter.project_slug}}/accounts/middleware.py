from accounts.utils import set_current_tenant, get_tenant_from_request


class MultitenantMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated:
            tenant = get_tenant_from_request(request)
            set_current_tenant(tenant)
        return self.get_response(request)
