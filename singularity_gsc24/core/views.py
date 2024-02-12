from rest_framework import status, views
from rest_framework.decorators import api_view
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


# SELECT id, ( 3959 * acos( cos( radians(37) ) * cos( radians( lat ) ) * cos( radians( lng ) - radians(-122) ) + sin( radians(37) ) * sin( radians( lat ) ) ) ) AS distance FROM markers HAVING distance < 25 ORDER BY distance LIMIT 0 , 20;

@api_view(["GET"])
def fish_location(request: Request) -> Response:
    if request.method == "GET":
        fish_name = request.query_params.get("fish_name")
        country = request.query_params.get("country")

        if fish_name and country:
            location = Location.objects.filter(
                fish_name__name=fish_name, country__name=country)
            return Response(LocationSerializer(instance=location, many=True).data)
        elif fish_name:
            location = Location.objects.filter(fish_name__name=fish_name)
            return Response(LocationSerializer(instance=location, many=True).data)
        elif country:
            location = Location.objects.filter(country__name=country)
            return Response(LocationSerializer(instance=location, many=True).data)

        return Response({"Message": "Fish name or Country name is required"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"Message": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def fish_location_v2(request: Request) -> Response:
    if request.method == "GET":
        fish_name = request.query_params.get("fish_name")
        country = request.query_params.get("country")

        if fish_name and country:
            location = Location.objects.filter(
                fish_name__name=fish_name, country__name=country)
            return Response(FishLocationSerializer(instance=location, many=True).data)
        elif fish_name:
            location = Location.objects.filter(fish_name__name=fish_name)
            return Response(FishLocationSerializer(instance=location, many=True).data)
        elif country:
            location = Location.objects.filter(country__name=country)
            return Response(FishLocationSerializer(instance=location, many=True).data)

        return Response({"Message": "Fish name or Country name is required"}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"Message": "Invalid request method"}, status=status.HTTP_400_BAD_REQUEST)
