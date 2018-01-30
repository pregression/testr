from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, reverse

from .models import User
from .admin import UserCreationForm


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            if user is not None:
                auth = authenticate(request, email=user.email, password=form.cleaned_data['password'])
                login(request, auth)
                return redirect(reverse('home'))
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})

