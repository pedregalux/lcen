from django.urls import path
from . import views
from .views import *
from django.conf.urls import handler404, handler500, handler403, handler400

urlpatterns = [
    path('', HomeView.as_view(), name='inicio'),
    path('enconstruccion/', EsperaView.as_view()),
    path('inicio/', HomeView.as_view(), name='inicio'),
    path('quees/', QueesView.as_view(), name='quees'),
    path('preguntasfrecuentes/', PreguntasView.as_view(), name='preguntasfrecuentes'),
    path('terminos/', TerminosView.as_view(), name='terminos'),
]

handler404 = 'inicio.views.error404'
handler500 = 'inicio.views.error500'
handler403 = 'inicio.views.error403'
handler400 = 'inicio.views.error400'
