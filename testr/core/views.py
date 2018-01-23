from django.shortcuts import render


def gpl_v3(request):
    return render(request, 'core/license.html', {})
