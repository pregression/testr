from django.shortcuts import render

def license(request):
    return render(request, 'core/license.html', {})
