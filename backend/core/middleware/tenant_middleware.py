from core.tenant.tenant import set_current_user, set_current_org


class TenantMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        set_current_user(request.user)
        set_current_org(request.session.get('org_id'))

        response = self.get_response(request)

        return response