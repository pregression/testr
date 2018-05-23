from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from core.models import Owner
from .models import Project
from .forms import NewProjectForm


@login_required
def index(request):
    user = request.user
    owner_ids = Owner.objects.filter(user_id__exact=user.id)
    projects = Project.objects.filter(owner_id__in=owner_ids)
    ctx = {'projects': projects}
    return render(request, 'projects/index.html', ctx)


@login_required
def new(request):
    if request.method == 'POST':
        form = NewProjectForm(request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            user = request.user
            try:
                owner = Owner.objects.get(user_id__exact=user.id)
            except Owner.DoesNotExist:
                owner = Owner.objects.create(user=user)
            project.owner_id = owner.id
            project.save()
            if project.id:
                return HttpResponseRedirect('/projects/%s' % project.name)
            else:
                return HttpResponseRedirect('/projects/')
    else:
        form = NewProjectForm()

    return render(request, 'projects/new.html', { 'form': form })


@login_required
def show(request, name):
    user = request.user
    owner_ids = Owner.objects.filter(user_id__exact=user.id)
    project = Project.objects.get(name__exact=name, owner_id__in=owner_ids)
    return render(request, 'projects/show.html', { 'project': project })
