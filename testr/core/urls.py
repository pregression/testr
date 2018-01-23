from django.urls import path

from . import views

urlpatterns = [
    path('license/', views.gpl_v3, name='license')
]