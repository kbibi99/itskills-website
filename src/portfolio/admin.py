from django.contrib import admin

# Register your models here.
from .models import (Portfolio, PortfolioTitle)

class PortfolioModelAdmin(admin.ModelAdmin):
    list_display = ["user", "title"]

    class Meta:
        model = Portfolio


admin.site.register(Portfolio, PortfolioModelAdmin)


class PortfolioTitleModelAdmin(admin.ModelAdmin):
    list_display = ["user"]

    class Meta:
        model = PortfolioTitle


admin.site.register(PortfolioTitle, PortfolioTitleModelAdmin)