from django import template
from propuestas.models import SubtemaPropuesta

register = template.Library()

@register.inclusion_tag('usuarios/convencionalespropuestasxsubtema.html')
def propuestasxsubtemaconvencionales():
    subtemas = SubtemaPropuesta.objects.filter(otros_temas_propuesta__isnull=False).distinct()
    return {'subtemas': subtemas}
