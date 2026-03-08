from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from visits.models import Visit
from forms_builder.models import FormResponse


class VisitDetailView(LoginRequiredMixin, DetailView):
    model = Visit
    template_name = "visits/visit_detail.html"
    context_object_name = "visit"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["forms"] = (
            FormResponse.objects
            .filter(visit=self.object)
            .select_related("form")
        )

        return context