from celery.utils.imports import instantiate
from app.celery import app
from django.http import HttpResponse
import csv 


@app.task
def send_message(message_pk: int):
    from messaging.models.message import Message

    instanse: Message = Message.objects.filter(pk=message_pk).first()
    if instanse is None:
        print(f'Message not found')
    else:
        print(f'Sending message: {str(instanse)}...')
        instanse.flag_sent = True
        instanse.save()
        print(f'Message sent: {str(instanse)}...')

