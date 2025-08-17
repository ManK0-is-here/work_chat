from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.views import View
from .forms import UserRegisterForm, CustomAuthForm


def user_home(request):
    """
    Домашняя страница пользователя.
    Если пользователь авторизован -> показываем user_home.html
    Если нет -> редиректим на страницу аутентификации
    """
    if request.user.is_authenticated:
        return render(request, 'user_home.html')
    else:
        return redirect("authentication")


class AuthenticationView(View):
    """
    Представление для логина и регистрации
    Одна страница с двумя формами
    """
    template_name = 'auth.html'

    def get(self, request):
        """Показываем пустые формы при GET-запросе"""
        if request.user.is_authenticated:
            return redirect('user_home')  # если юзер уже вошел — на главную

        login_form = CustomAuthForm()
        register_form = UserRegisterForm()
        return render(request, self.template_name, {
            'login_form': login_form,
            'register_form': register_form,
        })

    def post(self, request):
        """
        Обрабатываем POST-запросы:
        - Если нажата кнопка login → пытаемся авторизовать
        - Если нажата кнопка register → пытаемся зарегистрировать
        """
        if request.user.is_authenticated:
            return redirect('user_home')

        # Передаём данные в обе формы
        login_form = CustomAuthForm(request, data=request.POST)
        register_form = UserRegisterForm(request.POST)

        # 🔹 Обработка логина
        if 'login' in request.POST:  # проверяем name="login" у кнопки
            if login_form.is_valid():
                username = login_form.cleaned_data.get('username')
                password = login_form.cleaned_data.get('password')

                # Пытаемся авторизовать
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)  # вход
                    messages.success(request, f"Добро пожаловать, {user.username}!")
                    return redirect('user_home')
                else:
                    messages.error(request, "Неверные учетные данные")

            # Если форма невалидна → показать ошибки
            return render(request, self.template_name, {
                'login_form': login_form,
                'register_form': register_form,
            })

        # 🔹 Обработка регистрации
        elif 'register' in request.POST:  # проверяем name="register" у кнопки
            if register_form.is_valid():
                # Сохраняем пользователя
                user = register_form.save()
                # Автоматически логиним
                login(request, user)
                messages.success(request, f"Добро пожаловать, {user.username}! Регистрация завершена.")
                return redirect('user_home')
            else:
                messages.error(request, "Проверьте введенные данные")

        # Если что-то пошло не так — снова показываем страницу
        return render(request, self.template_name, {
            'login_form': login_form,
            'register_form': register_form,
        })


def logout_view(request):
    """
    Выход пользователя
    """
    logout(request)
    messages.success(request, "Вы успешно вышли из системы")
    return redirect('authentication')
