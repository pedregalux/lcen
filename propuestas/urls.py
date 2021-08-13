from django.urls import path
from . import views
from propuestas.views import *
from propuestas.forms import *
#from django.contrib.auth.decorators import login_required



urlpatterns=[
    path('verpropuestas/', views.VerPropuestasView.as_view(), name='ver_propuestas'),
    path('verpropuestas/<pk>', views.VerPropuestaView.as_view(), name='ver_propuesta'),
    path('crearpropuestas/', (PropuestaWizardView.as_view(FORMS2)), name='crearpropuestas'),
    # path('crearpropuesta/', views.CrearPropuestaView.as_view(), name='crear_propuesta'),
]
