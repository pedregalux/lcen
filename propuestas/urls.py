from django.urls import path
from . import  views



urlpatterns=[
    path('verpropuestas/',views.VerPropuestasView.as_view(), name='verpropuestas'),
    path('verpropuestas/<pk>',views.VerPropuestaView.as_view(), name='verpropuesta'),
    path('crearpropuesta/',views.CrearPropuestaView.as_view(), name='crearpropuesta'),
]
