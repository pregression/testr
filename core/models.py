from django.db import models
from django.utils.timezone import now

from custom_auth.models import User

class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Organization(TimeStampedModel):
    name = models.CharField(max_length=255, db_index=True)
    users = models.ManyToManyField(User, through='Membership', related_name='memberships')


class Membership(TimeStampedModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date_joined = models.DateField(default=now)


class Owner(TimeStampedModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
