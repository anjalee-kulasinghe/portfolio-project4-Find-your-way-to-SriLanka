from django.shortcuts import render
from django.views import View

class CityGuide(View):
    def get(self, request):
        return render(request, 'cityguide/cityguide.html')
