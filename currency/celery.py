from __future__ import absolute_import

import logging
import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency.settings')
app = Celery('currency')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

LOG = logging.getLogger(__name__)

app.conf.beat_schedule = {
    'currency_sync_engine': {
        'task': 'currency.scheduled_task.tasks.currency_sync_engine',
        'schedule': crontab(hour='*')  # execute every hour
    }
}


@app.task(bind=True)
def debug_task(self):
    LOG.info('Request: {0!r}'.format(self.request))
