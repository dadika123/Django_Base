import hashlib
import random

from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from authapp.models import User


class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['placeholder'] = 'Введите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class ShopUserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'age', 'email',
                  'avatar', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите ваше имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите вашу фамилию'
        self.fields['age'].widget.attrs['placeholder'] = 'Введите ваш возраст'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите ваш email'
        self.fields['avatar'].widget.attrs['placeholder'] = 'Фото профиля'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Подтвердите пароль'

        for field_name, field in self.fields.items():
            if field_name == 'avatar':
                field.widget.attrs['class'] = 'form-control-file py-4'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
            field.help_text = ''

    def save(self):
        user = super(ShopUserRegisterForm, self).save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class ShopUserProfileForm(UserChangeForm):
    avatar = forms.ImageField(widget=forms.FileInput())

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'age', 'email',
                  'avatar',)

    def __init__(self, *args, **kwargs):
        super(UserChangeForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True
        for field_name, field in self.fields.items():
            if field_name == 'avatar':
                field.widget.attrs['class'] = 'custom-file-input'
            else:
                field.widget.attrs['class'] = 'form-control py-4'
