from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User


def signup(request):
    return HttpResponse('<h1>Signup</h1>')


def signin(request):
    return HttpResponse('<h1>Signin</h1>')
