from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='projects_index'),
    path('new/', views.new, name='projects_new'),
    path('<str:name>/', views.show, name='projects_show'),
]