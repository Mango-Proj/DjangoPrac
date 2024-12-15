from django.urls import path
from . import views

app_name = 'Questionnaire'

urlpatterns = [
    # ex: /Questionnaire/
    path('', views.index, name='index'),
    # ex: /Questionnaire/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # ex: /Questionnaire/5/results/
    path('<int:question_id>/result/', views.results, name='result'),
    # ex: /Questionnaire/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
