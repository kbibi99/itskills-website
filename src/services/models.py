from __future__ import unicode_literals

from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.


class Services(models.Model):
    user=models.ForeignKey(User, default=1)
    # main_title=models.CharField(max_length=250, blank=True, null=True)
    # quote=models.CharField(max_length=250, blank=True, null=True)
    title=models.CharField(max_length=250, blank=True, null=True)
    body=models.CharField(max_length=500, blank=True, null=True)
    icon=models.CharField(max_length=50, blank=True, null=True)
    # activity=models.BooleanField(default=False)

    def __unicode__(self):
        return self.title