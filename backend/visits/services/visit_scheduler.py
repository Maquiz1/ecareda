from datetime import timedelta
from visits.models import Visit
from visits.models import ProjectVisitSchedule


def generate_subject_visits(subject):

    schedules = ProjectVisitSchedule.objects.filter(
        project=subject.project
    )

    baseline = subject.enrollment_date

    for schedule in schedules:

        scheduled = baseline + timedelta(days=schedule.days_from_baseline)

        Visit.objects.create(
            subject=subject,
            visit_type=schedule.visit_type,
            visit_number=schedule.visit_number,
            scheduled_date=scheduled,
            window_start=scheduled - timedelta(days=schedule.window_before),
            window_end=scheduled + timedelta(days=schedule.window_after),
        )