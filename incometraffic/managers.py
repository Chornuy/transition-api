from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.db.models import Sum
from django.utils.datetime_safe import datetime
from moneyed import Money

from incometraffic.constants import DEFAULT_CURRENCY, DELIVERED_MESSAGE_STATUS


class ProjectLimitQuerySet(models.QuerySet):
    pass


class ProjectLimitManager(models.Manager):
    def get_queryset(self):
        return ProjectLimitQuerySet(self.model, using=self._db)


class ProxyApiEndpointQuerySet(models.QuerySet):
    pass


class ProxyApiEndpointManager(models.Manager):
    def get_queryset(self):
        return ProxyApiEndpointQuerySet(self.model, using=self._db)

    def get_current_projects(self, user):
        return self.get_queryset().filter(user=user)

    def check_if_unique(self, url, user):
        try:
            self.get_queryset().get(endpoint=url, user=user)
            return False
        except ObjectDoesNotExist:
            return True


class IncomingMessageQuerySet(models.QuerySet):
    def total_sum_amount(self):
        return self.aggregate(Sum("amount"))

    def group_by_proxy_api(self, proxy_api_endpoint):
        return self.filter(proxy_project=proxy_api_endpoint)

    def filter_by_status(self, status):
        return self.filter(status=status)

    def filter_by_range_time(self, time_range):
        start_time = datetime.now() - time_range
        now = datetime.now()
        return self.filter(delivered_time__gte=start_time, delivered_time__lte=now)


class IncomingMessageManager(models.Manager):
    def get_queryset(self):
        return IncomingMessageQuerySet(self.model, using=self._db)

    def filter_by_range_time(self, time_range):
        return self.get_queryset().filter_by_range_time(time_range)

    def total_sum_amount(self):
        return self.get_queryset().total_sum_amount()

    def group_by_proxy_api(self, proxy_api_endpoint):
        return self.get_queryset().group_by_proxy_api(proxy_api_endpoint).values("proxy_project")

    def filter_by_status(self, status):
        return self.get_queryset().filter_by_status(status)

    def get_amount_per_limit(self, time_range, proxy_api):
        result = (
            self.get_queryset()
            .filter_by_range_time(time_range)
            .group_by_proxy_api(proxy_api)
            .filter_by_status(DELIVERED_MESSAGE_STATUS)
            .total_sum_amount()
        )
        if result["amount__sum"]:
            return Money(result["amount__sum"], DEFAULT_CURRENCY)
        return result["amount__sum"]

    def check_if_unique(self, name, user):
        try:
            self.get_queryset().get(name=name, user=name)
            return False
        except ObjectDoesNotExist:
            return True
