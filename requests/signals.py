from django.db.models.signals import post_save
from django.dispatch import receiver
from accounts.models import User
from .models import VisitRequestCart

@receiver(post_save, sender=User)
def create_visit_cart(sender, instance, created, **kwargs):
    if created:
        VisitRequestCart.objects.create(user=instance)