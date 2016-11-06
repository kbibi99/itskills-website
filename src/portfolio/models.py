from __future__ import unicode_literals

from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.


# Create your models here.
class Portfolio(models.Model):
    user=models.ForeignKey(User, default=1)
    title=models.CharField(max_length=500, blank=True, null=True)
    description=models.CharField(max_length=500, blank=True, null=True)
    picture = models.ImageField()
    # activity=models.BooleanField(default=False)

    def __unicode__(self):
        return '%s' % (self.user)

class PortfolioTitle(models.Model):
    user = models.ForeignKey(User, default=1)
    quote_text = models.CharField(max_length=250, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.user)