from rest_framework import serializers
from rest_framework.fields import CharField

from . import models


class FishSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Fish
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    name = FishSerializer(required=True)
    country = CountrySerializer(required=True)

    class Meta:
        model = models.Location
        fields = '__all__'
