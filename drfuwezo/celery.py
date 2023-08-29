from __future__ import absolute_import, unicode_literals
import os
from celery import Celery



# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drfuwezo.settings')

app = Celery('drfuwezo')

# Load task modules from all registered Django app configs.
app.config_from_object('django.conf:settings', namespace='CELERY')

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))