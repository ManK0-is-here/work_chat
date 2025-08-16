from django.shortcuts import render, redirect
from django.contrib.auth.views import *
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegisterForm, CustomAuthForm


def user_home(request):
    return render(request, "user_home.html")


def authentication_view(request):
    """
    Обработка входа и регистрации
    """
    if request.user.is_authenticated:
        return redirect('user_home')

    login_form = CustomAuthForm(request, request.POST or None)
    register_form = UserRegisterForm(request.POST or None)
    
    if request.method == 'POST':
        if 'login' in request.POST:
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('user_home')
                else:
                    messages.error(request, "Неверные учетные данные")
        
        elif 'register' in request.POST:
            if register_form.is_valid():
                user = register_form.save()
                login(request, user)
                messages.success(request, f"Регистрация завершена! Добро пожаловать {user.username}.")
                return redirect('user_home')
    
    context = {
        'login_form': login_form,
        'register_form': register_form,
    }
    return render(request, 'auth.html', context)


@login_required
def logout_view(request):
    """Выход пользователя"""
    logout(request)
    messages.success(request, "Вы успешно вышли из системы")
    return redirect('authentication')