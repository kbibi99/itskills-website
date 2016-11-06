from django.db.models import Q
from django.shortcuts import get_object_or_404, render

# from posts import views as PostsViews
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from services.models import Services
from about_us.models import AboutUs
from portfolio.models import *
from team.models import TeamTitle,Profile
from team.views import *
from posts.views import *
from posts.models import *

from .models import *


# Create your views here.


def home_list(request):
    # PostsViews.post_list(request)
    # AboutUsViews.about_us_list(request)
    homeQuery = Home.objects.all()
    serv_Query = Services.objects.all()
    commentQuery=ItComment.objects.all()
    about_usQuery=AboutUs.objects.all()
    portfolioTitleQuery=PortfolioTitle.objects.all()
    portfolioQuery=Portfolio.objects.all()
    teamTitleQuery=TeamTitle.objects.all()
    teamQuery=Profile.objects.all()

# posts method
    today = timezone.now().date()
    queryset_list = Post.objects.active() #.order_by("-timestamp")
    if request.user.is_staff or request.user.is_superuser:
        queryset_list = Post.objects.all()
    
    query = request.GET.get("q")
    if query:
        queryset_list = queryset_list.filter(
                Q(title__icontains=query)|
                Q(content__icontains=query)|
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
                ).distinct()
    paginator = Paginator(queryset_list, 8) # Show 25 contacts per page
    page_request_var = "page"
    page = request.GET.get(page_request_var)
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        queryset = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        queryset = paginator.page(paginator.num_pages)


    # context = {
    #     "posts_list": queryset, 
    #     "posts_title": "List",
    #     "posts_page_request_var": page_request_var,
    #     "posts_today": today,
    # }

# end post method

    context = {
        "home_list": homeQuery,
        "services_list": serv_Query,
        "about_us_list":about_usQuery,
        "portfolio_title":portfolioTitleQuery,
        "portfolio_list":portfolioQuery,
        "team_title":teamTitleQuery,
        "team_list":teamQuery,
        "comment_list":commentQuery,
        "posts_list": queryset, 
        "posts_title": "List",
        "posts_page_request_var": page_request_var,
        "posts_today": today,
    }
    return render(request, "home/index.html", context)
