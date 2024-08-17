from celery import shared_task

@shared_task
def minus(x, y):
    return x - y
