from django import template
from evaluaciones.models import CategoriaNorma

register = template.Library()

@register.inclusion_tag('evaluaciones/normasxcategoria.html')
def normasxcategoria():
    categorias = CategoriaNorma.objects.filter().distinct()
    return {'categorias': categorias}
