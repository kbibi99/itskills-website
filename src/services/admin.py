from django.contrib import admin
from .models import Services
# Register your models here.


class ServicesModelAdmin(admin.ModelAdmin):
    list_display = ["title", "icon"]

    class Meta:
        model = Services


admin.site.register(Services, ServicesModelAdmin)