from rest_framework import views
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .models import *
from .serializers import *


class FishNamesAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        return Response(FishNamesSerializer(instance=Fish.objects.all(), many=True).data)


class CountryNamesAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        return Response(CountrySerializer(instance=Country.objects.all(), many=True).data)


class LocationAPIView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request: Request) -> Response:
        return Response(LocationSerializer(instance=Location.objects.all(), many=True).data)
