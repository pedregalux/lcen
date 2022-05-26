from django import template
from evaluaciones.models import CategoriaNorma,TagNorma

register = template.Library()

@register.inclusion_tag('evaluaciones/normasxcategoria.html')
def normasxcategoria():
    categorias = CategoriaNorma.objects.filter().distinct()
    return {'categorias': categorias}

@register.inclusion_tag('evaluaciones/simbolosxcategorias.html')
def simbolosxcategorias():
    simbolosnormas = TagNorma.objects.all()
    return {'simbolosnormas': simbolosnormas}
