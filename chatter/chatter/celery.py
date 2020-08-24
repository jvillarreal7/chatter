"""Celery init."""

from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

# Default Django settings module for celery.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatter.settings')

app = Celery('chatter')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
