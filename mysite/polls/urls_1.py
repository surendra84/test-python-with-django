
from django.urls import path
from . import views_1

app_name = 'polls'
urlpatterns = [
    # ex: /polls/
    path('', views_1.index, name='index'),
    # ex: /polls/5/
    path('<int:question_id>/', views_1.details, name='detail'),
    # ex: /polls/5/results/
    path('<int:question_id>/results', views_1.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views_1.vote, name='vote')
]