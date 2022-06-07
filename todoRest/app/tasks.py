import time

from celery import shared_task


@shared_task
def my_multiply(x, y):
    time.sleep(10)
    return x * y