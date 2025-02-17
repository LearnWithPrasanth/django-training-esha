from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required(login_url='accounts:signin')
def home(request):
    return render(request, 'newsfeed/home.html')


@login_required(login_url='accounts:signin')
def something(request):
    return render(request, 'newsfeed/home.html')
