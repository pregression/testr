from django.shortcuts import render

from .models import Project


def index(request):
    projects = Project.objects.all()
    ctx = {'projects': projects}
    return render(request, 'projects/index.html', ctx)
