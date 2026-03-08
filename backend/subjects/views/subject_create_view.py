from django.urls import reverse_lazy
from subjects.models import Subject
from subjects.forms import SubjectForm
from core.views.tenant_create_view import TenantCreateView
from visits.services.visit_scheduler import generate_subject_visits


class SubjectCreateView(TenantCreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subjects/subject_form.html"
    success_url = reverse_lazy("subjects:subject_list")
    
    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["request"] = self.request
        return kwargs
    
    def save(self, *args, **kwargs):

        is_new = self.pk is None

        super().save(*args, **kwargs)

        if is_new:
            generate_subject_visits(self)