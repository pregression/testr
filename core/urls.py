from django.urls import path, include, re_path

from . import views

urlpatterns = [
    path('license/', views.gpl_v3, name='license'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]
