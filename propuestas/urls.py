from django.urls import path
from .views import *
from . import  views



urlpatterns=[
    path('verpropuestas/',views.VerPropuestasView.as_view(), name='ver_propuestas'),
    path('verpropuestas/<pk>',views.VerPropuestaView.as_view(), name='ver_propuesta'),
    path('crearpropuesta/',views.CrearPropuestaView.as_view(), name='crear_propuesta'),
]
