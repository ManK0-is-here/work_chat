from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import *
# from django.contrib.auth import login

# class HomeView(TemplateView):
#     template_name = 'home.html'

def home(request):
    return render(request, "home.html")

def test(request):
    return render(request, 'test.html')