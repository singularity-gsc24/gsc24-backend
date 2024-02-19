from django.urls import path

from core import views

urlpatterns = [
    path('fish-names/', views.FishNamesAPIView.as_view(), name="fish_names"),
    path('county-names/', views.CountryNamesAPIView.as_view(), name="country_names"),
    path('location/', views.LocationAPIView.as_view(), name="location"),
    path('fish-location/', views.fish_location, name="fish-location"),
    path('fish-location-v2/', views.fish_location_v2, name="fish-location-v2"),
]
