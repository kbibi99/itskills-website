from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import AboutUs


# Create your views here.

def about_us_list(request):
    
    about_Query = AboutUs.objects.all()


    context = {
        "object_list": about_Query,
    }
    return render(request, "about_us/index.html", context)
