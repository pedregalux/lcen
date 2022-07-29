from django import template
from evaluacionesinternacionales.models import CategoriaNormaInt,TagNormaInt

register = template.Library()

@register.inclusion_tag('evaluacionesinternacionales/normasxcategoriaint.html')
def normasxcategoriaint():
    categoriasint = CategoriaNormaInt.objects.filter().distinct()
    return {'categoriasint': categoriasint}

# @register.inclusion_tag('evaluaciones/simbolosxcategorias.html')
# def simbolosxcategorias():
#     simbolosnormas = TagNorma.objects.all()
#     return {'simbolosnormas': simbolosnormas}
