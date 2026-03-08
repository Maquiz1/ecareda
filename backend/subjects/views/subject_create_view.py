from django.urls import reverse_lazy
from subjects.models import Subject
from subjects.forms import SubjectForm
from core.views.tenant_create_view import TenantCreateView


class SubjectCreateView(TenantCreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subjects/subject_form.html"
    success_url = reverse_lazy("subjects:subject_list")