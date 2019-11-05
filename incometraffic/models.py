import uuid

from django.contrib.postgres.fields import DateTimeRangeField, JSONField
from django.db import models

# Create your models here.
from django.utils import timezone
from djmoney.models.fields import MoneyField

from incometraffic.constants import ENDPOINT_STATUSES, MESSAGE_STATUSES, PROCESSING_MESSAGE_STATUS
from incometraffic.managers import IncomingMessageManager, ProjectLimitManager, ProxyApiEndpointManager
from users.models import User


class ProxyApiEndpoint(models.Model):
    name = models.CharField(blank=False, null=None, max_length=200)
    endpoint = models.URLField(unique=True, null=False, blank=False)
    status = models.CharField(choices=ENDPOINT_STATUSES, max_length=200)

    created_time = models.DateTimeField(blank=False, null=False, default=timezone.now)
    updated_time = models.DateTimeField(blank=False, null=False, default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    headers = JSONField(null=True)

    objects = ProxyApiEndpointManager()

    def __str__(self):
        return f"user: {self.user}, endpoint: {self.endpoint}"


class ProjectLimit(models.Model):

    time_limit = models.DurationField()
    amount = MoneyField(max_digits=19, decimal_places=4, default_currency="UAH")
    created_time = models.DateTimeField(blank=False, null=False, default=timezone.now)
    updated_time = models.DateTimeField(blank=False, null=False, default=timezone.now)
    endpoint = models.ForeignKey(ProxyApiEndpoint, on_delete=models.CASCADE, null=False, blank=False)
    objects = ProjectLimitManager()

    def __str__(self):
        return f"amount: {self.amount}, time limit type:{self.time_limit.total_seconds()}"


class IncomingMessage(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_time = models.DateTimeField(blank=False, null=False, default=timezone.now)
    status = models.CharField(choices=MESSAGE_STATUSES, default=PROCESSING_MESSAGE_STATUS, max_length=200)
    delivered_time = models.DateTimeField(null=True, default=None)
    proxy_project = models.ForeignKey(ProxyApiEndpoint, on_delete=models.CASCADE)
    response_message = JSONField(null=True)
    request_data = JSONField(null=True)
    amount = MoneyField(max_digits=19, decimal_places=4, default_currency="UAH")

    objects = IncomingMessageManager()
