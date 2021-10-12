from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('',          views.index,    name='index'),
    path('new/',      views.new,      name='answer'),
    path('post/',     views.post,     name='post'),
    path('results/',  views.results,  name='results'),
    path('corrects/', views.corrects, name='corrects')
    ]