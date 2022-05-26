from django.db.models.signals import post_save
from django.dispatch import receiver, Signal
from django.core.signals import request_finished
from django.conf import settings

from rest_framework.authtoken.models import Token


post_done_todo = Signal()


@receiver(post_done_todo)
def print_taski_done_shod(sender, user=None, **kwargs):
    print(user)
    print("taski done shod")


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


# @receiver(request_finished)
# def my_callback(sender, **kwargs):
#     print("kwargs", kwargs)
#     print(sender)
#     print("Request finished!")
