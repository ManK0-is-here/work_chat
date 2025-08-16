from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "home.html")

def in_dev(r):
    return render(r, "in_dev.html")

def register(r):
    return render(r, "auth.html")
