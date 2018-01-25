from django.urls import path
from django.contrib.auth.views import LoginView

from .admin import AuthenticationForm


urlpatterns = [
    path('login/', LoginView.as_view(authentication_form=AuthenticationForm))
]
