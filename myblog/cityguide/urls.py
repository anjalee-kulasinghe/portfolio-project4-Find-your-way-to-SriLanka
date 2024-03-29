from django.urls import path
from .views import CityGuide

urlpatterns = [
    path('', CityGuide.as_view(), name='cityguide'),
]