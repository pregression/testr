from django.db import models

from custom_auth.models import User

class Owner(models.Model):
    user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    
