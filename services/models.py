from django.db import models


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    image = models.ImageField(upload_to="services", verbose_name="Imagen")
    content = models.TextField(verbose_name="Contenido")

    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"

    def __str__(self):
        return self.title
