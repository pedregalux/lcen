from django.urls import path
from . import views
from .views import *


urlpatterns = [
    path('', HomeView.as_view(), name='inicio'),
    path('enconstruccion/', EsperaView.as_view()),
    path('inicio/', HomeView.as_view(), name='inicio'),
    path('quees/', QueesView.as_view(), name='quees'),
    path('preguntasfrecuentes/', PreguntasView.as_view(), name='preguntasfrecuentes'),
    path('ensayos/', EnsayosView.as_view(), name='ensayos'),
    path('ensayo-tomouno/', EnsayotomounoView.as_view(), name='ensayo-tomouno'),
    path('ensayo-tomodos/', EnsayotomodosView.as_view(), name='ensayo-tomodos'),
    path('ensayo-tomotres/', EnsayotomotresView.as_view(), name='ensayo-tomotres'),
    path('ensayo-tomocuatro/', EnsayotomocuatroView.as_view(), name='ensayo-tomocuatro'),
    path('ensayo-tomocinco/', EnsayotomocincoView.as_view(), name='ensayo-tomocinco'),
    path('terminos/', TerminosView.as_view(), name='terminos'),
]
