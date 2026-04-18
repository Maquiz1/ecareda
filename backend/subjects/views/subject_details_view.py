from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from subjects.models import Subject
from visits.models import Visit


class SubjectDetailView(LoginRequiredMixin, DetailView):
    model = Subject
    template_name = "subjects/subject_detail.html"
    context_object_name = "subject"

    def get_queryset(self):
        org_id = self.request.session.get("org_id")
        project_id = self.request.session.get("project_id")
        
        qs = Subject.objects.filter(is_deleted=False)
        
        if org_id:
            qs = qs.filter(organization_id=org_id)
        if project_id:
            qs = qs.filter(project_id=project_id)
            
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["visits"] = (
            Visit.objects
            .filter(subject=self.object)
            .order_by("visit_number")
        )

        return context