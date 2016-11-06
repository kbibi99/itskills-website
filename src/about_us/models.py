from __future__ import unicode_literals

from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.
class AboutUs(models.Model):
    user=models.ForeignKey(User, default=1)
    body_1=models.CharField(max_length=500, blank=True, null=True)
    body_2=models.CharField(max_length=500, blank=True, null=True)
    user_experience = models.CharField(max_length=50, blank=True, null=True)
    mobile_development = models.CharField(max_length=50, blank=True, null=True)
    training_session = models.CharField(max_length=50, blank=True, null=True)
    fun = models.CharField(max_length=50, blank=True, null=True)
    # activity=models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % (self.user)