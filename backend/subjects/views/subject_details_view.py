from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from subjects.models import Subject
from visits.models import Visit

class SubjectDetailView(LoginRequiredMixin, DetailView):
    model = Subject
    template_name = "subjects/subject_detail.html"
    context_object_name = "subject"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["visits"] = Visit.objects.filter(
            subject=self.object,
            is_deleted=False
        ).order_by("visit_number")
        return context