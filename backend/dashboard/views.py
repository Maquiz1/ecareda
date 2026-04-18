from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

from subjects.models import Subject
from visits.models import Visit
from forms_builder.models import FormResponse


class DashBoardView(LoginRequiredMixin, TemplateView):

    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        org_id = self.request.session.get("org_id")
        project_id = self.request.session.get("project_id")
        country_id = self.request.session.get("country_id")
        site_id = self.request.session.get("site_id")

        # Global filtering for all metrics
        subjects_qs = Subject.objects.filter(is_deleted=False)
        visits_qs = Visit.objects.all()
        forms_qs = FormResponse.objects.all()

        if org_id:
            subjects_qs = subjects_qs.filter(organization_id=org_id)
            visits_qs = visits_qs.filter(subject__organization_id=org_id)
            forms_qs = forms_qs.filter(visit__subject__organization_id=org_id)

        if country_id:
            subjects_qs = subjects_qs.filter(site__country_id=country_id)
            visits_qs = visits_qs.filter(subject__site__country_id=country_id)
            forms_qs = forms_qs.filter(visit__subject__site__country_id=country_id)

        if site_id:
            subjects_qs = subjects_qs.filter(site_id=site_id)
            visits_qs = visits_qs.filter(subject__site_id=site_id)
            forms_qs = forms_qs.filter(visit__subject__site_id=site_id)

        if project_id:
            subjects_qs = subjects_qs.filter(project_id=project_id)
            visits_qs = visits_qs.filter(subject__project_id=project_id)
            forms_qs = forms_qs.filter(visit__subject__project_id=project_id)

        context["total_subjects"] = subjects_qs.count()
        context["total_visits"] = visits_qs.count()

        context["completed_visits"] = visits_qs.filter(status="completed").count()
        context["open_visits"] = visits_qs.filter(status="open").count()

        context["completed_forms"] = forms_qs.filter(status="completed").count()
        context["pending_forms"] = forms_qs.filter(status="pending").count()

        context["recent_subjects"] = subjects_qs.order_by("-id")[:5]
        context["recent_visits"] = visits_qs.order_by("-visit_date")[:5]

        return context