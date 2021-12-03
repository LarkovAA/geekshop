from django import forms
from authnapp.forms import ShopUserRegistrtForm, ShopUserProfilForm
from authnapp.models import ShopUser


class UserAdminRegisterForm(ShopUserRegistrtForm):

    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar', 'age')

class UserAdminProfilForm(ShopUserProfilForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4', 'readonly': False}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4', 'readonly': False}))

    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar', 'age')