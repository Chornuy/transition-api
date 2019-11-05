from datetime import timedelta

from django.core.exceptions import ObjectDoesNotExist
from djmoney.money import Money
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from incometraffic.constants import DEFAULT_CURRENCY
from incometraffic.models import IncomingMessage, ProjectLimit, ProxyApiEndpoint
from incometraffic.validators import validate_for_incoming_limit, validate_unique_endpoint


class MoneyField(serializers.Field):
    def to_representation(self, obj):
        return obj.amount

    def to_internal_value(self, data):
        return Money(data, DEFAULT_CURRENCY)


class DurationInSeconds(serializers.Field):
    def to_representation(self, obj):
        print(obj)
        return obj.total_seconds()

    def to_internal_value(self, data):
        return timedelta(seconds=data)


class ProxyProjectField(serializers.Field):
    def to_representation(self, obj):
        return obj.name

    def to_internal_value(self, data):
        try:
            return ProxyApiEndpoint.objects.get(name=data)
        except ObjectDoesNotExist:
            raise ValidationError("no such proxy project registered")


class ProjectLimitSerializer(serializers.ModelSerializer):
    time_limit = DurationInSeconds(required=True, allow_null=False)
    amount = MoneyField(required=True, allow_null=False)

    def create(self, validated_data):
        print(validated_data)

    def update(self, instance, validated_data):
        pass

    class Meta:
        model = ProjectLimit
        fields = ["id", "time_limit", "amount"]
        read_only_fields = ("id", "created_time", "updated_time")


class ProxyApiEndpointSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200, allow_blank=False, allow_null=False)
    endpoint = serializers.URLField(allow_blank=False, allow_null=False, validators=[validate_unique_endpoint])
    limits = ProjectLimitSerializer(many=True, required=False, source="projectlimit")

    user = serializers.SerializerMethodField("_user")

    def _user(self, obj=None):
        request = self.context.get("request", None)
        if request:
            return request.user
        if hasattr(obj, "user"):
            return obj.user.email

    def create(self, validated_data):
        endpoint = ProxyApiEndpoint(**validated_data)
        endpoint.user = self._user()
        endpoint.save()

        if "projectlimit" in validated_data.keys():
            endpoint_limits = validated_data.pop("projectlimit")
            for endpoint_limit in endpoint_limits:
                endpoint_limit["endpoint"] = endpoint
                limit = ProjectLimit.objects.create(**endpoint_limit)
                endpoint.projectlimit_set.add(limit)

        endpoint.save()

        return endpoint

    def update(self, instance, validated_data):
        instance.endpoint = validated_data.get("endpoint")
        instance.name = validated_data.get("name")
        instance.save()
        return instance

    class Meta:
        model = ProxyApiEndpoint
        fields = ["id", "name", "endpoint", "limits", "user", "created_time", "updated_time"]
        read_only_fields = ("id", "created_time", "updated_time")


class IncomingMessageSerializer(serializers.ModelSerializer):

    id = serializers.UUIDField(read_only=True)
    created_time = serializers.DateTimeField(read_only=True)
    status = serializers.CharField(read_only=True)
    delivered_time = serializers.DateTimeField(read_only=True, default=None)
    proxy_project = ProxyProjectField()
    response_message = serializers.DictField(read_only=True)
    request_data = serializers.DictField(required=True)
    amount = MoneyField(required=True)

    def validate(self, data):
        validate_for_incoming_limit(data["proxy_project"].projectlimit_set.all(), data["proxy_project"])

        return data

    def create(self, validated_data):
        return IncomingMessage.objects.create(**validated_data)

    class Meta:
        model = IncomingMessage
        fields = [
            "id",
            "created_time",
            "delivered_time",
            "proxy_project",
            "response_message",
            "amount",
            "request_data",
            "status",
        ]
        read_only_fields = ("id", "created_time", "delivered_time", "status")
