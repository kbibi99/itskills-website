from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import Portfolio, PortfolioTitle


# Create your views here.

def portfolio_list(request):
    
    portfolio_Query = Portfolio.objects.all()
    portfolio_title_Query = PortfolioTitle.objects.all()


    context = {
        "object_title": portfolio_title_Query,
        "object_list": portfolio_Query,
    }
    return render(request, "portfolio/index.html", context)
