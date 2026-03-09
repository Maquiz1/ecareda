from django.utils.timezone import now
from visits.models import Visit


def update_visit_status():

    today = now().date()

    visits = Visit.objects.exclude(status="completed")

    for visit in visits:

        if today < visit.window_start:
            new_status = "scheduled"

        elif visit.window_start <= today <= visit.window_end:
            new_status = "window_open"

        else:
            new_status = "overdue"

        if visit.status != new_status:
            visit.status = new_status
            visit.save(update_fields=["status"])