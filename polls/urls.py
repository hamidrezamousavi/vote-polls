from django.urls import path
from .views import IndexView, DetailView, vote, ResultsView
app_name='polls'
urlpatterns=[
    path('',IndexView.as_view(),name='index'),
    path('<int:pk>/',DetailView.as_view(),name='detail'),
    path('<int:question_id>/vote',vote,name='vote'),
    path('<int:pk>/results/',ResultsView.as_view(),name='results'),
    

]