from django.shortcuts import render
from django.views import View

class Food(View):
    def get(self, request):
        return render(request, 'food/food.html')
