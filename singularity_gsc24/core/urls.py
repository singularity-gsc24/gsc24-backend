from django.urls import path

from core import views

urlpatterns = [
    path('fishes/', views.FishAPIView.as_view(), name="fishes"),

]

# TODO: Add a url for Country, Location
