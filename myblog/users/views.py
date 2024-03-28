'''
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
'''
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .forms import UserRegisterForm

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html', {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        # Print request headers
        print(request.headers)

        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            # Handle form errors if needed
            return HttpResponse("Form is not valid")
