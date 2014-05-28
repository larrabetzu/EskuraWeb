from celery import Celery

celery = Celery('tasks')

@celery.task
def aktualizatu():
    print('ffff')