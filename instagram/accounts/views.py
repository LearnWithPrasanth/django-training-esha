from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .forms import RegistrationForm


class RegisterView(CreateView):
    form_class = RegistrationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('accounts:signin')

    def form_valid(self, form):
        response = super().form_valid(form)
        return response


def signin(request):
    return HttpResponse('sign in')
