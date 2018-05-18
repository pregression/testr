from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import CspReport


def gpl_v3(request):
    return render(request, 'core/license.html', {})


def terms(request):
    return render(request, 'core/terms.html', {})


def privacy(request):
    return render(request, 'core/privacy.html', {})


@csrf_exempt
def report_csp(request):
    if request.method == "POST":
        CspReport.objects.create(report=request.body.decode('utf8'))
        return HttpResponse('OK')
    return HttpResponse('No Content', status=204)
