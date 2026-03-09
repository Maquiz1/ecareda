from celery import shared_task
from visits.services.update_visit_status import update_visit_status


@shared_task
def update_visit_status_task():

    update_visit_status()