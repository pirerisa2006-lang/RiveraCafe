from django.shortcuts import render
from .models import Service


def services(request):
    return render(request, "services/services.html", {"services": Service.objects.all()})
