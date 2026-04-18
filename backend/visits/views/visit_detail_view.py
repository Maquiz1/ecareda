from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from visits.models import Visit
from forms_builder.models import FormResponse


class VisitDetailView(LoginRequiredMixin, DetailView):
    model = Visit
    template_name = "visits/visit_detail.html"
    context_object_name = "visit"

    def get_queryset(self):
        org_id = self.request.session.get("org_id")
        project_id = self.request.session.get("project_id")
        
        qs = Visit.objects.all()
        
        if org_id:
            qs = qs.filter(subject__organization_id=org_id)
        if project_id:
            qs = qs.filter(subject__project_id=project_id)
            
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["forms"] = (
            FormResponse.objects
            .filter(visit=self.object)
            .select_related("form")
        )

        return context