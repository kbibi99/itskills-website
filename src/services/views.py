from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Services
# Create your views here.

def services_list(request):
    
    serv_Query = Services.objects.all()


    context = {
        "object_list": serv_Query,
    }
    return render(request, "services/index.html", context)