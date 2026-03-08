from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse
from django.shortcuts import get_object_or_404

from visits.forms import VisitForm
from visits.models import Visit
from subjects.models import Subject


class VisitCreateView(LoginRequiredMixin, CreateView):
    model = Visit
    form_class = VisitForm
    template_name = "visits/visit_form.html"

    def dispatch(self, request, *args, **kwargs):
        self.subject = get_object_or_404(
            Subject.objects.filter(is_deleted=False),
            pk=self.kwargs["subject_id"]
        )
        return super().dispatch(request, *args, **kwargs)

    def get_initial(self):
        last_visit = (
            Visit.objects
            .filter(subject=self.subject)
            .order_by("-visit_number")
            .first()
        )

        next_number = 1 if not last_visit else last_visit.visit_number + 1

        return {"visit_number": next_number}

    def form_valid(self, form):
        form.instance.subject = self.subject
        return super().form_valid(form)

    def get_success_url(self):
        return reverse(
            "subjects:subject_detail",
            kwargs={"pk": self.subject.pk}
        )