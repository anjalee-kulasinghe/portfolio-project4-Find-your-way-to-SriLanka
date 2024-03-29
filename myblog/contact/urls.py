from django.urls import path
from .views import ContactView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
]