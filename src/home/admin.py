from django.contrib import admin
from .models import *
# Register your models here.


class HomeModelAdmin(admin.ModelAdmin):
    list_display = ["title_1", "title_2"]


    class Meta:
        model = Home


admin.site.register(Home, HomeModelAdmin)


class ItCommmentModelAdmin(admin.ModelAdmin):
    list_display = ["title"]


    class Meta:
        model = ItComment


admin.site.register(ItComment, ItCommmentModelAdmin)