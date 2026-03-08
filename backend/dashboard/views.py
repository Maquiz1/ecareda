from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from subjects.models import Subject
from visits.models import Visit
from forms_builder.models import FormResponse


class DashBoardView(LoginRequiredMixin, TemplateView):

    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = self.request.user

        subjects = Subject.objects.filter(
            organization=user.organization,
            is_deleted=False
        )

        visits = Visit.objects.filter(
            subject__organization=user.organization
        )

        forms = FormResponse.objects.filter(
            visit__subject__organization=user.organization
        )

        context["total_subjects"] = subjects.count()
        context["total_visits"] = visits.count()

        context["completed_visits"] = visits.filter(
            status="completed"
        ).count()

        context["open_visits"] = visits.filter(
            status="open"
        ).count()

        context["completed_forms"] = forms.filter(
            status="completed"
        ).count()

        context["pending_forms"] = forms.filter(
            status="pending"
        ).count()

        context["recent_subjects"] = subjects.order_by("-id")[:5]

        context["recent_visits"] = visits.order_by("-visit_date")[:5]

        return context