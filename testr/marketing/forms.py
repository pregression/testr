from django.forms import ModelForm, EmailInput
from .models import NewsletterSubscription


class NewNewsletterSubscription(ModelForm):
    class Meta:
        model = NewsletterSubscription
        fields = ['email']
        widgets = {
            'email': EmailInput(
                attrs={
                    'placeholder': 'Email address',
                    'class': 'NewsletterSubscription--input',
                }),
        }
