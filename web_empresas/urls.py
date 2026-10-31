"""URL configuration for web_empresas project."""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("store/", views.store, name="store"),
    path("privacy/", views.privacy, name="privacy"),
    # Cada app tiene su propio urls.py y se enlaza con include()
    path("blog/", include("blog.urls")),
    path("services/", include("services.urls")),
    path("social/", include("social.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
