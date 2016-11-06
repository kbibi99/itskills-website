from django.conf.urls import url
from django.contrib import admin

from .views import (
    home_list,
    )

urlpatterns = [
    url(r'^$', home_list, name='list'),
]