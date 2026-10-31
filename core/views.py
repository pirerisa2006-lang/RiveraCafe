from django.shortcuts import render


def index(request):
    return render(request, template_name='core/index.html')


def about(request):
    return render(request, template_name='core/about.html')


def contact(request):
    return render(request, template_name='core/contact.html')


def privacy(request):
    return render(request, template_name='core/privacy.html')


def store(request):
    return render(request, template_name='core/store.html')
