from django.shortcuts import render
from .models import Redsocial


def redes(request):
    return render(request, "social/social.html", {"redes": Redsocial.objects.all()})
