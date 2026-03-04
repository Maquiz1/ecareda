from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from subjects.models import Subject
from visits.models import Visit


class SubjectDetailView(LoginRequiredMixin, DetailView):
    model = Subject
    template_name = "subjects/subject_detail.html"
    context_object_name = "subject"

    def get_queryset(self):
        """
        Ensure users only access subjects belonging to their organization
        and exclude soft-deleted records.
        """
        return Subject.objects.filter(
            organization=self.request.user.organization,
            is_deleted=False
        )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["visits"] = (
            Visit.objects.filter(
                subject=self.object,
                is_deleted=False
            )
            .select_related("subject")
            .order_by("visit_number")
        )

        return context
    
    
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from core.mixins import TenantQuerysetMixin
from subjects.models import Subject


class SubjectDetailView(LoginRequiredMixin, TenantQuerysetMixin, DetailView):
    model = Subject
    template_name = "subjects/subject_detail.html"
    context_object_name = "subject"