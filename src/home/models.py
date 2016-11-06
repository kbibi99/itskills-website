from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models

# Create your models here.


class Home(models.Model):
    user=models.ForeignKey(User, default=1)
    title_1=models.CharField(max_length=250, blank=True, null=True)
    title_2=models.CharField(max_length=250, blank=True, null=True)
    body=models.CharField(max_length=500, blank=True, null=True)
    background_img=models.FileField()
    activity=models.BooleanField(default=False)

    def __unicode__(self):
        return self.title_1 + '_'+ self.title_2




class ItComment(models.Model):
    user = models.ForeignKey(User, default=1)
    title=models.CharField(max_length=500, blank=True, null=True)
    comment=models.CharField(max_length=500, blank=True, null=True)
    activity=models.BooleanField(default=False)


