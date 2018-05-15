from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import NewNewsletterSubscription


def index(request):
    newsletter_form = NewNewsletterSubscription()
    return render(request, 'marketing/index.html', { 'newsletter_form': newsletter_form })


def subscribe(request):
    if request.method == 'POST':
        form = NewNewsletterSubscription(request.POST)
        if form.is_valid():
            subscription = form.save()
            if subscription.id is not None:
                messages.add_message(request, messages.SUCCESS, "Thank you for your support!")
            else:
                messages.add_message(request, messages.ERROR, subscription.message)
        else:
            messages.add_message(request, messages.ERROR, form.errors['email'])

    referer = request.META.get('HTTP_REFERER')
    if referer is not None:
        return HttpResponseRedirect(referer)
    return redirect('marketing_home')
