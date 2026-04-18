from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView, ListView
from visits.models import Visit
from forms_builder.models import FormResponse


class VisitListView(LoginRequiredMixin, ListView):
    model = Visit
    template_name = "visits/visit_list.html"
    context_object_name = "visits"
    
    def get_queryset(self):
        org_id = self.request.session.get("org_id")
        project_id = self.request.session.get("project_id")
        site_id = self.request.session.get("site_id")
        
        qs = Visit.objects.all()
        
        if org_id:
            qs = qs.filter(subject__organization_id=org_id)
        if project_id:
            qs = qs.filter(subject__project_id=project_id)
        if site_id:
            qs = qs.filter(subject__site_id=site_id)
            
        return qs.order_by("subject_id")
