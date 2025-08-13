from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

def home(request):
    register_form = RegisterForm()
    login_form = AuthenticationForm()
    
    return render(request, "home.html", {
        'register_form': register_form,
        'login_form': login_form
    })

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_home')
    return redirect('home')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_home')
    return redirect('home')

@login_required
def user_home(request):
    return render(request, "user_home.html")