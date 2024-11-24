from django.shortcuts import render, redirect
from .forms import ContactForm
from django.urls import reverse

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():  # Verificar si el formulario es válido
            # Recuperar los datos del formulario de forma segura
            name = request.POST.get("name", "")
            email = request.POST.get("email", "")
            content = request.POST.get("content", "")
            
            # Aquí puedes hacer lo que quieras con los datos, como enviar un email
            print(f"Nombre: {name}, Email: {email}, Contenido: {content}")

            # Redirigir con un parámetro GET 'ok' para mostrar un mensaje de éxito
            return redirect(f"{reverse('contact')}?ok=True")
    else:
        form = ContactForm()  # Si la solicitud es GET, mostramos el formulario vacío

    # Renderizamos el template
    return render(request, "contact/contact.html", {"form": form})