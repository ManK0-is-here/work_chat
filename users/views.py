from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from .forms import UserRegisterForm, CustomAuthForm


def user_home(request):
    """
    Домашняя страница пользователя
    """
    if request.user.is_authenticated:
        return render(request, 'user_home.html')
    return redirect('login')


class RegisterView(View):
    """
    Регистрация
    """
    template_name = 'register.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('user_home')
        form = UserRegisterForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('user_home')

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) 
            messages.success(request, f"Добро пожаловать, {user.username}! Вы успешно зарегистрировались.")
            return redirect('user_home')
        else:
            return render(request, self.template_name, {'form': form})


class LoginView(View):
    """
    Вход
    """
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('user_home')
        form = CustomAuthForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('user_home')

        form = CustomAuthForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Добро пожаловать, {user.username}!")
            return redirect('user_home')
        else:
            messages.error(request, "Неверное имя пользователя или пароль")
            return render(request, self.template_name, {'form': form})


def logout_view(request):
    """Выход"""
    logout(request)
    messages.success(request, "Вы вышли из системы")
    return redirect('login')
