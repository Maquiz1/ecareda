from datetime import timedelta
from django.utils.timezone import now
from dateutil.relativedelta import relativedelta

from subjects.models import Subject
from visits.models import Visit, ProjectVisitSchedule


def generate_recurring_visits():

    today = now().date()

    subjects = Subject.objects.select_related("project")

    for subject in subjects:

        schedules = ProjectVisitSchedule.objects.filter(
            project=subject.project,
            recurrence_months__gt=0
        )

        for schedule in schedules:

            last_visit = Visit.objects.filter(
                subject=subject,
                visit_type=schedule.visit_type
            ).order_by("-scheduled_date").first()

            if not last_visit:
                continue

            next_date = last_visit.scheduled_date + relativedelta(
                months=schedule.recurrence_months
            )

            if next_date <= today:

                Visit.objects.create(
                    subject=subject,
                    visit_type=schedule.visit_type,
                    visit_number=last_visit.visit_number + 1,
                    scheduled_date=next_date,
                    window_start=next_date - timedelta(days=schedule.window_before),
                    window_end=next_date + timedelta(days=schedule.window_after),
                )