from bitlab_store.celery import celery_app
from time import sleep


@celery_app.task
def send_email(email, **kwargs):
    sleep(15)
