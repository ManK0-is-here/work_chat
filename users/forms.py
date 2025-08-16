from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
)
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError



class UserRegisterForm(UserCreationForm):
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
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        
        return cleaned_data

class CustomAuthForm(AuthenticationForm):
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