from django.conf.urls import url
from django.contrib import admin

from .views import (
    about_us_list,
    )

urlpatterns = [
    url(r'^$', about_us_list, name='list'),
]