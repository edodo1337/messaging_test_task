import os

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
RABBITMQ_HOST = os.getenv('RABBITMQ_HOST', 'localhost')

# Celery
CELERY_BROKER_URL = 'amqp://localhost'.format(RABBITMQ_HOST)
CELERY_RESULT_BACKEND = 'redis://{}:6379'.format(REDIS_HOST)
# CELERY_RESULT_BACKEND = 'django-db'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
# CELERY_TIMEZONE = TIME_ZONE
# CELERY_TASK_ALWAYS_EAGER = TEST
CELERY_ENABLE_UTC = False
DJANGO_CELERY_BEAT_TZ_AWARE = False