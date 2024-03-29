from django.shortcuts import render
from django.views import View
from .forms import ContactForm

"""
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Redirect or render a success page
            return render(request, 'contact/success.html')
    else:
        form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form})
"""


class ContactView(View):
    # Handling GET requests to display the concat form
    def get(self, request):
        # Instantiate the UserRegisterForm
        form = ContactForm()
        # Render the registration form template with the form object
        return render(request, 'contact/contact.html', {'form': form})

    # Handling POST requests to process form submission
    def post(self, request):
        # Instantiate the ContactForm with the form data from the POST request
        form = ContactForm(request.POST)

        # Check if the form data is valid
        if form.is_valid():
            return render(request, 'contact/success.html')
        else:
            # If form data is invalid, re-render the contact form template with the form and errors
            return render(request, 'contact/contact.html', {'form': form})