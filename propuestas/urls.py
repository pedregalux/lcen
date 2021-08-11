from django.urls import path
from . import views
from propuestas.views import *
from propuestas.forms import *



urlpatterns=[
    path('verpropuestas/', views.VerPropuestasView.as_view(), name='ver_propuestas'),
    path('verpropuestas/<pk>', views.VerPropuestaView.as_view(), name='ver_propuesta'),
    path('contactwizard/', ContactWizard.as_view(FORMS)),
    path('crearpropuesta/', views.CrearPropuestaView.as_view(), name='crear_propuesta'),
    path('crearpropuestas/', PropuestaWizardView.as_view(FORMS2), name='crearpropuestas'),
]
