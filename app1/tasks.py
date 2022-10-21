from __future__ import absolute_import, unicode_literals
from time import sleep



from celery import shared_task

@shared_task
def add(x, y):
    print('add called from server')
    sleep(10)
    print('awake')
    return x + y

