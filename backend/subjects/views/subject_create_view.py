from django.views.generic import CreateView
from django.urls import reverse_lazy
from subjects.models import Subject
from subjects.forms import SubjectForm


class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subjects/subject_form.html"
    success_url = reverse_lazy("subject_list")

    def form_valid(self, form):
        # assign organization from selected project
        form.instance.organization = form.instance.project.organization
        return super().form_valid(form)