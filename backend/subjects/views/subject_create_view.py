from django.views.generic import CreateView
from django.urls import reverse_lazy
from subjects.forms import SubjectForm
from subjects.models import Subject


class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "subjects/subject_form.html"
    success_url = reverse_lazy("subject_list")