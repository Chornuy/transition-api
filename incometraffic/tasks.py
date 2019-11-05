
import requests
from celery import shared_task
from django.utils.datetime_safe import datetime

from incometraffic.constants import DELIVERED_MESSAGE_STATUS, FAILED_MESSAGE_STATUS
from incometraffic.models import IncomingMessage


@shared_task
def send_incoming_message(message_pk):
    incoming_message = IncomingMessage.objects.get(pk=message_pk)
    try:
        response = requests.post(incoming_message.proxy_project.endpoint, incoming_message.request_data)
        incoming_message.delivered_time = datetime.now()
        incoming_message.status = DELIVERED_MESSAGE_STATUS
        incoming_message.save()
    except requests.exceptions.RequestException as e:
        incoming_message.status = FAILED_MESSAGE_STATUS
        incoming_message.save()
