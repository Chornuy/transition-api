from django.http import Http404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from incometraffic.constants import SUCCESS_API_MESSAGE_STATUS
from incometraffic.models import ProxyApiEndpoint, IncomingMessage
from incometraffic.serializers import IncomingMessageSerializer, ProxyApiEndpointSerializer

from .tasks import send_incoming_message


class ProjectView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        endpoints = [endpoint for endpoint in ProxyApiEndpoint.objects.filter(user=request.user)]
        return Response(ProxyApiEndpointSerializer(endpoints, many=True).data, status.HTTP_200_OK)

    def post(self, request, format=None):
        endpoint_serializer = ProxyApiEndpointSerializer(data=request.data, context={"request": request})
        if endpoint_serializer.is_valid(raise_exception=True):
            endpoint_entry = endpoint_serializer.save()
        return Response(
            {"result": SUCCESS_API_MESSAGE_STATUS, "data": ProxyApiEndpointSerializer(endpoint_entry).data},
            status=status.HTTP_201_CREATED,
        )


class ProjectDetails(APIView):
    permission_classes = (IsAuthenticated,)

    @staticmethod
    def get_object(pk):
        try:
            return ProxyApiEndpoint.objects.get(pk=pk)
        except ProxyApiEndpoint.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        api_endpoint = self.get_object(pk)
        serializer = ProxyApiEndpointSerializer(api_endpoint)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        api_endpoint = self.get_object(pk)
        serializer = ProxyApiEndpointSerializer(api_endpoint, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        api_endpoint = self.get_object(pk)
        api_endpoint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SendMessage(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        serializer = IncomingMessageSerializer(data=request.data)
        if serializer.is_valid():
            incoming_message = serializer.save()
            send_incoming_message.delay(str(incoming_message.pk))
            return Response(IncomingMessageSerializer(incoming_message).data, status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ViewMessage(APIView):

    @staticmethod
    def get_object(pk):
        try:
            return IncomingMessage.objects.get(pk=pk)
        except IncomingMessage.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        incoming_message = self.get_object(pk)
        return Response(IncomingMessageSerializer(incoming_message).data, status.HTTP_200_OK)

