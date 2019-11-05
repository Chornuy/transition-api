from django.core.exceptions import ObjectDoesNotExist
from rest_framework.exceptions import ValidationError

from incometraffic.models import IncomingMessage, ProxyApiEndpoint


def validate_for_incoming_limit(limits, proxy_api):
    for limit in limits:
        total_amount = IncomingMessage.objects.get_amount_per_limit(limit.time_limit, proxy_api)
        if total_amount and total_amount >= limit.amount:
            raise ValidationError(
                f"amount limit exeeded ({int(limit.amount.amount)}/{int(limit.time_limit.total_seconds())}sec)"
            )


def validate_unique_endpoint(url):
    try:
        ProxyApiEndpoint.objects.get(endpoint=url)
        raise ValidationError("Such endpoint already register")
    except ObjectDoesNotExist:
        pass
