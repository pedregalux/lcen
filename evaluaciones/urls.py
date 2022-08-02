from django.urls import path
from . import  views
from evaluaciones.views import *



urlpatterns=[
    path('homeevaluaciones/',views.VerHomeEvaluacionesView.as_view(), name='homeevaluaciones'),
    path('homeevaluaciones/<pk>',views.VerHomeEvaluacionView.as_view(), name='homeevaluacion'),
    path('verevaluaciones/',views.VerEvaluacionesView.as_view(), name='verevaluaciones'),
    path('verevaluaciones/<pk>',views.VerEvaluacionView.as_view(), name='verevaluacion'),
    path('verorgsevaluadoras/',views.VerOrgsEvalView.as_view(), name='verorgsevaluadoras'),
    path('verorgevaluadora/<pk>',views.VerOrgEvalView.as_view(), name='verorgevaluadora'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('search/<pk>', SearchResultView.as_view(), name='search_result'),
]
