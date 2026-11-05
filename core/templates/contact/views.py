import logging

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect, render

from .forms import ContactForm

logger = logging.getLogger(__name__)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            email = form.cleaned_data["email"]
            text = form.cleaned_data["message"]
            body = f"Nombre: {name}\nEmail: {email}\n\nMensaje:\n{text}"
            try:
                send_mail(
                    f"Nuevo mensaje de contacto de {name}",
                    body,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_RECIPIENT],
                )
            except Exception:
                logger.exception("No se pudo enviar el correo de contacto")
                messages.error(
                    request,
                    "No se pudo enviar el mensaje. Inténtalo de nuevo más tarde.",
                )
            else:
                messages.success(request, "¡Mensaje enviado! Te responderemos pronto.")
                return redirect("contact")
    else:
        form = ContactForm()
    return render(request, "contact/contact.html", {"form": form})
