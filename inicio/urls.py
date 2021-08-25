from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', LandingView.as_view()),
    path('enconstruccion/', EsperaView.as_view()),
    path('inicio/', HomeView.as_view(), name='inicio'),
    path('quees/', QueesView.as_view(), name='quees'),
    path('preguntasfrecuentes/', PreguntasView.as_view(), name='preguntasfrecuentes'),
]
