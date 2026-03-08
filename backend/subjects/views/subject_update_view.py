from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from subjects.models import Subject
from subjects.forms import SubjectForm
from core.mixins import TenantQuerysetMixin


class SubjectUpdateView(LoginRequiredMixin, TenantQuerysetMixin, UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subjects/subject_form.html"

    def get_success_url(self):
        # return reverse_lazy("subjects:subject_detail", kwargs={"pk": self.object.pk})
        return reverse_lazy("subjects:subject_list")