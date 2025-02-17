from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def signup(request):
    # request_data = request.scheme
    # print(request_data)
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username):
            return render(request, 'accounts/signup.html')

        User.objects.create_user(
            first_name=first_name,
            username=username,
            password=password
        )
        return redirect('signin')
    return render(request, 'accounts/signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('newsfeed:home')
    return render(request, 'accounts/signin.html')


"""
def anyview():
    Instead of using this way
    if username is not empty:
        register user
    else:
        return username is required

    Using this way is much better
    if user is empty:
        return "Username is required"
        
    register logic

"""
