from django.urls import path

from . import views

app_name = 'quiz'
urlpatterns = [
    path('index/',   views.index,   name='index'),
    path('new/',    views.new,      name='post_answer'),
    path('results/', views.results, name='results')
    ]