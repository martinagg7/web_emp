from django.shortcuts import render
from .forms import ContactForm  # Asegúrate de tener este formulario definido en forms.py

from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm

def contacto(request):
    if request.method == "POST":
        form = ContactForm(request.POST)  
        if form.is_valid():  # verif formulario es válido
            
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
          
            print(f"Nombre: {name}, Email: {email}, Contenido: {content}")


            return redirect(f"{reverse('contacto')}?ok=True")
    else:
        form = ContactForm()  

    # Renderizamos el template
    return render(request, "core/contacto.html", {"form": form})