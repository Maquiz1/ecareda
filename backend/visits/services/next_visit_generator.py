from datetime import timedelta
from dateutil.relativedelta import relativedelta

from visits.models import Visit, ProjectVisitSchedule


def create_next_visit(visit):

    subject = visit.subject

    schedule = ProjectVisitSchedule.objects.filter(
        project=subject.project,
        visit_type=visit.visit_type
    ).first()

    if not schedule:
        return

    # manual scheduling
    if schedule.recurrence_months == 0:
        return

    next_date = visit.scheduled_date + relativedelta(
        months=schedule.recurrence_months
    )

    exists = Visit.objects.filter(
        subject=subject,
        scheduled_date=next_date,
        visit_type=visit.visit_type
    ).exists()

    if exists:
        return

    Visit.objects.create(
        subject=subject,
        visit_type=visit.visit_type,
        visit_number=visit.visit_number + 1,
        scheduled_date=next_date,
        window_start=next_date - timedelta(days=schedule.window_before),
        window_end=next_date + timedelta(days=schedule.window_after),
        status="scheduled"
    )