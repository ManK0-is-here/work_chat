from django.shortcuts import render
from django.contrib.auth.views import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

def user_home_page(request):
    return render(request, "user_home.html")