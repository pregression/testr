from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.contrib.postgres.fields import JSONField
from django.utils.timezone import now
from json import loads

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


class CspReport(TimeStampedModel):
    report = JSONField(encoder=DjangoJSONEncoder)

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        report = getattr(self, 'report')
        if isinstance(report, str):
            self.report = loads(report)

        return super(CspReport, self).save(force_insert, force_update, using, update_fields)

    def __str__(self):
        return "CSP Report: {0} at {1}".format(self.id, self.created_at)
 