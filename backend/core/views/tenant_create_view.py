from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView


class TenantCreateView(LoginRequiredMixin, CreateView):

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs