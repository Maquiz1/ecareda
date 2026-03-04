from core.tenant.tenant import set_current_user


class TenantMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        set_current_user(request.user)

        response = self.get_response(request)

        return response