from .models import Redsocial


def redes_sociales(request):
    """Disponible en todas las plantillas (pie de página)."""
    return {"redes": Redsocial.objects.all()}
