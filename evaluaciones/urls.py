from django.urls import path
from . import  views
from evaluaciones.views import *



urlpatterns=[
    path('homeevaluaciones/',views.VerHomeEvaluacionesView.as_view(), name='homeevaluaciones'),
     path('verevaluaciones/',views.VerEvaluacionesView.as_view(), name='verevaluaciones'),
     path('verevaluaciones/<pk>',views.VerEvaluacionView.as_view(), name='verevaluacion'),
]
