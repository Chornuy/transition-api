from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.


class TestApiEndpoint(APIView):
    def post(self, request, format=None):
        print(request.data)
        return Response(request.data, status=status.HTTP_201_CREATED)
