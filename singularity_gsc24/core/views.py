from json import JSONDecodeError

from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status, views
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from .models import *
from .serializers import CountrySerializer, FishSerializer

# Create your views here.


class FishAPIView(views.APIView):
    serializer_class = FishSerializer

    # def get_serializer_context(self) -> dict:
    #     return {'request': self.request, 'format': self.format_kwarg, 'view': self}

    # def get_serializer(self, *args, **kwargs):
    #     kwargs['context'] = self.get_serializer_context()
    #     print(kwargs, "HERE")
    #     return self.serializer_class(*args, **kwargs)

    def post(self, request) -> Response | JsonResponse:
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

    def get(self, request) -> Response:
        return Response(FishSerializer(instance=Fish.objects.all(), many=True).data)

# TODO: Add a view for Country, Location
