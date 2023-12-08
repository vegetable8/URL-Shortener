import os

from celery import Celery

def make_celery():
    celery = Celery(__name__)
    celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
    celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
    
    return celery

celery = make_celery()