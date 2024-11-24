from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ContactForm
from django.core.mail import EmailMessage

def contact(request):
    # print('Tipo de petición: {}'.format(request.method))
    contact_form = ContactForm()

    if request.method == 'POST':
        # Estoy enviando el formulario
        contact_form = ContactForm(data=request.POST)

        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')  # Usamos 'content' en lugar de 'message'

            # Enviar el correo electrónico
            email = EmailMessage(
                'Mensaje de contacto recibido',
                'Mensaje enviado por {} <{}>: \n\n{}'.format(name, email, content),
                email,
                ['112fd567f5cafd@inbox.mailtrap.io'],
                reply_to=[email],
            )

            try:
                email.send()  # Intentar enviar el correo
                # Está todo OK
                return redirect(reverse('contact') + '?ok')
            except:
                # Ha habido un error y retorno a ERROR
                return redirect(reverse('contact') + '?error')

    return render(request, 'contact/contact.html', {'form': contact_form})