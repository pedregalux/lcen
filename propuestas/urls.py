from django.urls import path
from . import views
from propuestas.views import *
from propuestas.forms import *



urlpatterns=[
    path('verpropuestas/', views.VerPropuestasView.as_view(), name='ver_propuestas'),
    path('verpropuestas/<pk>', views.VerPropuestaView.as_view(), name='ver_propuesta'),
    path('crearpropuesta/', views.CrearPropuestaView.as_view(), name='crear_propuesta'),
    path('crearpropuestas/', PropuestaWizardView.as_view([PropuestaForm1, PropuestaForm2, PropuestaForm3, PropuestaForm4, PropuestaForm5, PropuestaForm6, PropuestaForm7]), name='crearpropuestas'),
]
