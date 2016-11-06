from django.conf.urls import url
from django.contrib import admin

from .views import (
    portfolio_list,
    )

urlpatterns = [
    url(r'^$', portfolio_list, name='list'),
]