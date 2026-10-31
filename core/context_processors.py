from django.conf import settings
from urllib.parse import quote


def whatsapp(request):
    number = getattr(settings, "WHATSAPP_NUMBER", "")
    text = quote(getattr(settings, "WHATSAPP_MESSAGE", ""))
    return {"whatsapp_url": f"https://wa.me/{number}?text={text}"}
