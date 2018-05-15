from django.db import models
from django.utils.timezone import now

from custom_auth.models import User
from core.models import TimeStampedModel, Owner


class Project(TimeStampedModel):
    name = models.CharField(max_length=255, db_index=True)
    users = models.ManyToManyField(User)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    deactivated_at = models.DateTimeField(null=True)
    activated_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

    def deactivate(self):
        self.is_active = False
        self.deactivated_at = now()
        self.save()
        return self

    def activate(self):
        self.is_active = True
        self.activated_at = now()
        self.save()
        return self

    def is_abandoned(self):
        return len(self.users.all()) == 0
