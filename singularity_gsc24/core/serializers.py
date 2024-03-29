from rest_framework import serializers

from . import models


class FishNamesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fish
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    fish_name = FishNamesSerializer(required=True)
    country = CountrySerializer(required=True)

    class Meta:
        model = models.Location
        fields = '__all__'


class FishLocationSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='fish_name')
    lat = serializers.FloatField(source='latitude')
    lng = serializers.FloatField(source='longitude')

    class Meta:
        model = models.Location
        fields = ('address', 'lat', 'lng')
