from core import views
from django.urls import path

urlpatterns = [
    path('fish-names/', views.FishNamesAPIView.as_view(), name="fish_names"),
    path('county-names/', views.CountryNamesAPIView.as_view(), name="country_names"),
    path('location/', views.LocationAPIView.as_view(), name="location"),
]

# TODO: Add a url for Country, Location
