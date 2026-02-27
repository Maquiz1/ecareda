from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from subjects.models import Subject

class SubjectListView(LoginRequiredMixin, ListView):
    model = Subject
    template_name = "subjects/subject_list.html"
    context_object_name = "subjects"

    def get_queryset(self):
        return Subject.objects.filter(is_deleted=False)

