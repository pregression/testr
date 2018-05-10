from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="marketing_home"),
    path('subscribe/', views.subscribe, name="new_subscription"),
]
