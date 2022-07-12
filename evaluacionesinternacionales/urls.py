from django.urls import path
from . import  views
from evaluacionesinternacionales.views import *



urlpatterns=[
    path('evaluacionesint/',views.VerEvaluacionesIntView.as_view(), name='evaluaciones_int'),
    path('evaluacionesint/<pk>',views.VerEvaluacionIntView.as_view(), name='verevaluacion_int'),
]
