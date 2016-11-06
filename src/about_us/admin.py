from django.contrib import admin

from .models import AboutUs


# Register your models here.


class AboutUsModelAdmin(admin.ModelAdmin):
    list_display = ["user", "user_experience","mobile_development","training_session","fun"]


    class Meta:
        model = AboutUs


admin.site.register(AboutUs, AboutUsModelAdmin)
