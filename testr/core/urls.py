from django.urls import path

from . import views

urlpatterns = [
    path('license/', views.license, name='license')
]