from django.urls import path
from django.conf.urls import url
from . import views
from propuestas.views import *
from propuestas.forms import *
#from django.contrib.auth.decorators import login_required



urlpatterns=[
    path('verpropuestas/', views.VerPropuestasView.as_view(), name='ver_propuestas'),
    path('verpropuestas/<pk>', views.VerPropuestaView.as_view(), name='ver_propuesta'),
    path('verpropuestas/<pk>', views.CardPropuestaView.as_view(), name='cardpropuesta'),
    path('crearpropuestas/', PropuestaWizardView.as_view(), name='crearpropuestas'),
    path('propapoyo/<pk>', ApoyoView, name='prop_apoyo'),
    # path('crearpropuesta/', views.CrearPropuestaView.as_view(), name='crear_propuesta'),
]
