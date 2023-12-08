from .worker import celery
import time

@celery.task
def sleepyTime():
    time.sleep(5)
    return "hasasd"
