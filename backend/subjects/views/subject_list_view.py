from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from subjects.models import Subject


class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = "subjects/subject_list.html"
    context_object_name = "subjects"

    def get_queryset(self):
        org_id = self.request.session.get("org_id")
        project_id = self.request.session.get("project_id")
        site_id = self.request.session.get("site_id")
        
        qs = Subject.objects.filter(is_deleted=False)
        
        if org_id:
            qs = qs.filter(organization_id=org_id)
        if project_id:
            qs = qs.filter(project_id=project_id)
        if site_id:
            qs = qs.filter(site_id=site_id)
            
        return qs.select_related("site", "project").order_by("project__name", "site__name", "subject_id")