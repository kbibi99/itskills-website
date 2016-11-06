from __future__ import unicode_literals
from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.urlresolvers import reverse
from django.db.models.signals import pre_save
from django.utils.text import slugify

# Create your models here.

class TeamTitle(models.Model):
    user=models.ForeignKey(User, default=1)
    team_title= models.CharField(max_length=50, blank=True, null=True)
    team_description= models.CharField(max_length=500, blank=True, null=True)



class Profile(models.Model):
    user=models.ForeignKey(User, default=1)
    first_name= models.CharField(max_length=500, blank=True, null=True)
    last_name= models.CharField(max_length=500, blank=True, null=True)
    slug = models.SlugField(unique=True)
    owner_title= models.CharField(max_length=500, blank=True, null=True)
    owner_description= models.CharField(max_length=500, blank=True, null=True)
    company_title= models.CharField(max_length=500, blank=True, null=True)
    company_name=models.CharField(max_length=500, blank=True, null=True)
    born_date= models.CharField(max_length=500, blank=True, null=True)
    born_plase= models.CharField(max_length=500, blank=True, null=True)
    adress= models.CharField(max_length=500, blank=True, null=True)
    facebook= models.CharField(max_length=500, blank=True, null=True)
    twitter= models.CharField(max_length=500, blank=True, null=True)
    linkedin= models.CharField(max_length=500, blank=True, null=True)
    skype= models.CharField(max_length=500, blank=True, null=True)
    forsquare= models.CharField(max_length=500, blank=True, null=True)
    instagram= models.CharField(max_length=500, blank=True, null=True)
    picture_index=models.FileField()
    picture_cv=models.FileField()
    cv_pdf=models.FileField()

    def get_absolute_url(self):
        return reverse("team:detail", kwargs={"slug": self.slug})

    def __unicode__(self):
        return '%s-%s' % (self.first_name, self.last_name)


class Email(models.Model):
    owner=models.ForeignKey(Profile,default=1)
    e_mail= models.CharField(max_length=500, blank=True, null=True)
    active=models.BooleanField(default=False)

class PhoneNumber(models.Model):
    owner=models.ForeignKey(Profile,default=1)
    phone_number= models.CharField(max_length=500, blank=True, null=True)
    active=models.BooleanField(default=False)

class SotialNetAdress(models.Model):
    owner=models.ForeignKey(Profile,default=1)
    sotial_network_adress= models.CharField(max_length=500, blank=True, null=True)
    
    
class Education(models.Model):
    owner=models.ForeignKey(Profile,default=1)
    degree_name=models.CharField(max_length=500, blank=True, null=True)
    institute_name=models.CharField(max_length=500, blank=True, null=True)
    graduation_type=models.CharField(max_length=500, blank=True, null=True)
    description=models.CharField(max_length=500, blank=True, null=True)
    date_of_graduation=models.CharField(max_length=500, blank=True, null=True)
    period_of_studies=models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.owner)

class WorkExperience(models.Model):
    owner=models.ForeignKey(Profile,default=1)
    company_name=models.CharField(max_length=500, blank=True, null=True)
    work_period=models.CharField(max_length=500, blank=True, null=True)
    mission=models.CharField(max_length=500, blank=True, null=True)
    description01=models.CharField(max_length=500, blank=True, null=True)
    description02=models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.owner)

class InternShip(models.Model):
    owner=models.ForeignKey(Profile,default=1)
    company_name=models.CharField(max_length=500, blank=True, null=True)
    period=models.CharField(max_length=500, blank=True, null=True)
    mission=models.CharField(max_length=500, blank=True, null=True)
    description=models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.owner)

class Projects(models.Model):
    owner=models.ForeignKey(Profile,default=1)
    project_name=models.CharField(max_length=500, blank=True, null=True)
    project_type=models.CharField(max_length=500, blank=True, null=True)
    project_period=models.CharField(max_length=500, blank=True, null=True)
    used_technologies=models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.owner)

class SocialExperience(models.Model):
    owner=models.ForeignKey(Profile,default=1)
    comunity_name=models.CharField(max_length=500, blank=True, null=True)
    owner_title=models.CharField(max_length=500, blank=True, null=True)
    working_period=models.CharField(max_length=500, blank=True, null=True)
    description=models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.owner)

class Skill_title(models.Model):
    owner=models.ForeignKey(Profile,default=1)
    skill_title=models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%s %s' % (self.owner, self.skill_title)


class Skills(models.Model):
    skill_title=models.ForeignKey(Skill_title,default=1)
    skill_name=models.CharField(max_length=500, blank=True, null=True)
    skill_percent=models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.skill_title)

class Recongnitions(models.Model):
    owner=models.ForeignKey(Profile,default=1)
    title=models.CharField(max_length=500, blank=True, null=True)
    description=models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.owner)


class Interests(models.Model):
    owner=models.ForeignKey(Profile,default=1)
    title=models.CharField(max_length=500, blank=True, null=True)
    description=models.CharField(max_length=500, blank=True, null=True)

    def __unicode__(self):
        return '%s' % (self.owner)



def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Post.objects.filter(slug=slug).order_by("-id")
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" %(slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)



pre_save.connect(pre_save_post_receiver, sender=Profile)