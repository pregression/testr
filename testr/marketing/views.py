from django.shortcuts import render, redirect
from django.contrib import messages

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
    return redirect('marketing_home')
