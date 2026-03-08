from datetime import date
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from django.views import View

from subjects.models import Subject
from visits.models import Visit


class UnscheduledVisitCreateView(LoginRequiredMixin, View):

    def post(self, request, subject_id):

        subject = get_object_or_404(Subject, pk=subject_id)

        # determine next visit number
        last_visit = (
            Visit.objects
            .filter(subject=subject)
            .order_by("-visit_number")
            .first()
        )

        next_number = 1 if not last_visit else last_visit.visit_number + 1

        Visit.objects.create(
            subject=subject,
            visit_type="unscheduled",
            visit_number=next_number,
            visit_date=date.today(),
            is_unscheduled=True
        )

        messages.success(request, "Unscheduled visit created.")

        return redirect("subjects:subject_detail", pk=subject_id)