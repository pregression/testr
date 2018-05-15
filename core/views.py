from django.shortcuts import render


def gpl_v3(request):
    return render(request, 'core/license.html', {})


def terms(request):
    return render(request, 'core/terms.html', {})


def privacy(request):
    return render(request, 'core/privacy.html', {})
