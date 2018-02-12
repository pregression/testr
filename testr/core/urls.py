from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('testr.marketing.urls')),
    path('license/', views.gpl_v3, name='license'),
    path('terms/', views.terms, name='terms'),
    path('privacy/', views.privacy, name='privacy'),
]
