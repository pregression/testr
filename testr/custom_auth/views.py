from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse

from .models import User
from .admin import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            data = form.data

            user = User.objects.create(
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password'),
            )

            if user is not None:
                auth = authenticate(request, username=user.username, password=user.password)
                login(request, auth)
                return redirect(reverse('home'))
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

