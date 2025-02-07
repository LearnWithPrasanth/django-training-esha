from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def signup(request):
    # request_data = request.scheme
    # print(request_data)
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        User.objects.create(
            first_name=first_name,
            username=username,
            password=password
        )
    return HttpResponse('<h1>Signup</h1>')


def signin(request):
    return HttpResponse('<h1>Signin</h1>')
