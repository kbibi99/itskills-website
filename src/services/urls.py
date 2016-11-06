from django.conf.urls import url
from django.contrib import admin

from .views import (
    services_list,
    )

urlpatterns = [
    url(r'^$', services_list, name='list'),
]