import uuid

from django.db import models
from django_extensions.db.models import TimeStampedModel


class Model(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    class Meta:
        abstract = True


class Fish(Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Fishes"


class Country(Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Countries"


class Location(Model, TimeStampedModel):
    name = models.ForeignKey(Fish, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    population = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.name} - {self.country}"

    class Meta:
        verbose_name_plural = "Locations"
