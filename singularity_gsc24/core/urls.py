from core import views
from django.urls import path

urlpatterns = [
    path('fishes/', views.FishAPIView.as_view()),
]

# TODO: Add a url for Country, Location
