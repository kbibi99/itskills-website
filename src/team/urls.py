from django.conf.urls import url
from django.contrib import admin

from .views import team_detail

urlpatterns = [
    url(r'^(?P<slug>[\w-]+)/$', team_detail, name='detail'),
]
