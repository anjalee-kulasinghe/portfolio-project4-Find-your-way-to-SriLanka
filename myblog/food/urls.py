from django.urls import path
from .views import Food

urlpatterns = [
    path('', Food.as_view(), name='food'),
]