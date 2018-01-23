from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('marketing.urls')),
    path('license/', views.gpl_v3, name='license')
]