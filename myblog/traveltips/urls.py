from django.urls import path
from .views import TravelTips

urlpatterns = [
    path('', TravelTips.as_view(), name='traveltips'),
]