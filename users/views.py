from django.shortcuts import render, redirect
from django.contrib.auth.views import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def user_home(request):
    return render(request, "user_home.html")