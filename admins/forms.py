from django import forms
from django.contrib.auth.forms import UserCreationForm

from authnapp.forms import ShopUserRegistrtForm, ShopUserProfilForm
from authnapp.models import ShopUser
from product.models import Category, Product


class UserAdminRegisterForm(ShopUserRegistrtForm):

    avatar = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'avatar', 'age')

class UserAdminProfilForm(ShopUserProfilForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    class Meta:
        model = ShopUser
        fields = ('username', 'email', 'first_name', 'last_name', 'avatar', 'age')

    def __init__(self, *args, **kwargs):
        super(UserAdminProfilForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['username'].widget.attrs['readonly'] = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['avatar'].widget.attrs['class'] = 'custom-file-input'

class CategoryAdminRegisterForm(forms.ModelForm):
    id = forms.CharField(widget=forms.NumberInput(attrs={'readonly': False}))

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

class CategoryAdminUpdateForm(forms.ModelForm):
    id = forms.CharField(widget=forms.NumberInput(attrs={'readonly': False}))

    class Meta:
        model = Category
        fields = ('id', 'name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryAdminUpdateForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'

class ProductAdminRegisterForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ProductAdminRegisterForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'

class ProductAdminUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('__all__')

    def __init__(self, *args, **kwargs):
        super(ProductAdminUpdateForm, self).__init__(*args, **kwargs)

        # self.fields['id'].widget.attrs['readonly'] = False

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'