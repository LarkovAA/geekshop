import hashlib
import random

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.core.exceptions import ValidationError
from django import forms

from .models import ShopUser

class ShopUserLoginForm(AuthenticationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'password')

    def __init__(self, *args, **kwargs):
        super(ShopUserLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['password'].widget.attrs['password'] = 'Введите пароль'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

    # def clean_username(self):
    #     data = self.cleaned_data['username']
    #     if not data.isalpha():
    #         raise ValidationError('Имя пользователя не может содержать цифры')
    #     return data

class ShopUserRegistrtForm(UserCreationForm):
    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(ShopUserRegistrtForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['placeholder'] = 'Введите имя пользователя'
        self.fields['email'].widget.attrs['placeholder'] = 'Введите e-mail'
        self.fields['first_name'].widget.attrs['placeholder'] = 'Введите имя'
        self.fields['last_name'].widget.attrs['placeholder'] = 'Введите фамилию'
        self.fields['password1'].widget.attrs['placeholder'] = 'Введите пароль'
        self.fields['password2'].widget.attrs['placeholder'] = 'Повторите пароль'

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py'

    def save(self, commit=True):
        user = super(ShopUserRegistrtForm, self).save()
        user.is_active = False
        salt = hashlib.sha1(str(random.random()).encode('utf8')).hexdigest()[:6]
        user.activation_key = hashlib.sha1((user.email + salt).encode('utf8')).hexdigest()
        user.save()
        return user


class ShopUserProfilForm(UserChangeForm):
    avatar = forms.ImageField(widget=forms.FileInput(), required=False)
    age = forms.IntegerField(widget=forms.NumberInput(), required=False)

    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar', 'age')

    def __init__(self, *args, **kwargs):
        super(ShopUserProfilForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['readonly'] = True
        self.fields['email'].widget.attrs['readonly'] = True


        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'