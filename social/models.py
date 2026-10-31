from django.db import models


class Redsocial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    link = models.URLField(verbose_name="Enlace")

    class Meta:
        verbose_name = "red social"
        verbose_name_plural = "redes sociales"

    def __str__(self):
        return self.name
