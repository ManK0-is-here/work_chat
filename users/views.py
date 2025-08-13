from django.shortcuts import render, redirect
from django.contrib.auth.views import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, LoginForm

# class UserDoor():

@login_required
def user_home(self, request):
    return render(request, "user_home.html", {"user": request.user})

def home_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('user_home')
    else:
        form = LoginForm()
    
    return render(request, 'home.html', {'login_form': form})

def logout_view(self, request):
    logout(request)
    return redirect("home")