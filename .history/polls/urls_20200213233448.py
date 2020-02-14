from django.urls import path
from . import views


app_name = 'polls'
urlpatterns = [
    path('now/', views.ShowTimeView.as_view(), name='now'),

    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]

