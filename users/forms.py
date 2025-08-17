from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserRegisterForm(UserCreationForm):
    """
    Форма регистрации пользователя
    Наследуется от стандартной UserCreationForm
    """

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-styling',
            'placeholder': 'Email'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        """Настраиваем внешний вид полей"""
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-styling',
            'placeholder': 'Как вас будут звать'
        })
        self.fields['password1'].widget.attrs.update({
            'class': 'form-styling',
            'placeholder': 'Пароль'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-styling',
            'placeholder': 'Повторить пароль'
        })

    def clean(self):
        """Проверяем совпадение паролей"""
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")

        return cleaned_data

    def save(self, commit=True):
        """
        Переопределяем save(), чтобы сохранялся email
        Без этого email игнорировался бы
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]  # сохраняем email
        if commit:
            user.save()
        return user


class CustomAuthForm(AuthenticationForm):
    """
    Кастомная форма логина
    Просто настраиваем placeholder и css-класс
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-styling',
            'placeholder': 'Имя'
        })
        self.fields['password'].widget.attrs.update({
            'class': 'form-styling',
            'placeholder': 'Пароль'
        })
