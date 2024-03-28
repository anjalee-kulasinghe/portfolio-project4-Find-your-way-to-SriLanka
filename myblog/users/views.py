from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm

class RegisterView(View):
    # Handling GET requests to display the registration form
    def get(self, request):
        # Instantiate the UserRegisterForm
        form = UserRegisterForm()
        # Render the registration form template with the form object
        return render(request, 'users/register.html', {'form': form})

    # Handling POST requests to process form submission
    def post(self, request):
        # Instantiate the UserRegisterForm with the form data from the POST request
        form = UserRegisterForm(request.POST)

        # Check if the form data is valid
        if form.is_valid():
            # Save the form data to create a new user
            form.save()
            # Redirect the user to the index page upon successful registration
            return redirect('index')
        else:
            # If form data is invalid, render the registration form template with the form and errors
            return render(request, 'users/register.html', {'form': form})