from django.db.models.signals import post_save
from django.dispatch import receiver

from visits.models import Visit
from visits.services.next_visit_generator import create_next_visit


@receiver(post_save, sender=Visit)
def generate_next_visit(sender, instance, created, **kwargs):

    if instance.status == "completed":

        create_next_visit(instance)