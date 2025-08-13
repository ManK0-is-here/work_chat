from django.shortcuts import render, redirect
from django.contrib.auth.views import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm


def user_home(self, request):
    return render(request, "user_home.html")