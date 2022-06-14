import time

from django.core.mail import send_mail

from celery import shared_task


@shared_task
def my_multiply(x, y):
    time.sleep(10)
    return x * y

    
@shared_task
def async_send_mail(subject, message, email_from, recipient_list):
    return send_mail( subject, message, email_from, recipient_list )