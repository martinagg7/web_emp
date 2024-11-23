from django.shortcuts import render
from .forms import ContactForm  # Asegúrate de tener este formulario definido en forms.py

def contact(request):
    contact_form = ContactForm()
    return render(request, 'core/contact.html', {'form': contact_form})