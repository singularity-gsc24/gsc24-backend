from json import JSONDecodeError

from django.http import JsonResponse
from rest_framework import status, views
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from .models import *
from .serializers import CountrySerializer, FishSerializer


class FishAPIView(views.APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = FishSerializer

    def post(self, request: Request) -> Response | JsonResponse:
        try:
            data = JSONParser().parse(request)
            serializer = FishSerializer(data=data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except JSONDecodeError:
            return JsonResponse({"result": "error", "message": "Json decoding error"}, status=400)

    def get(self, request: Request) -> Response:
        return Response(FishSerializer(instance=Fish.objects.all(), many=True).data)

# TODO: Add a view for Country, Location
