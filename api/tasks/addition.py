from celery import shared_task


@shared_task(queue="dataset")
def addition(x, y):
    return x + y
