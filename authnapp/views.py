from django.shortcuts import render, HttpResponseRedirect
from authnapp.forms import ShopUserLoginForm, ShopUserLogoutForm
from django.contrib import auth
from django.urls import reverse

# Create your views here.
def login(request):
    title = 'Ввод данных'
    if request.method == 'POST':
        login_form = ShopUserLoginForm(data=request.POST)
        if login_form.is_valid():
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        login_form = ShopUserLoginForm()

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authnapp/login.html', content)

def register(request):
    title = 'Регистрация'
    if request.method == 'POST':
        register_form = ShopUserLogoutForm(data=request.POST)
        if register_form.is_valid():
            register_form.save()
            return HttpResponseRedirect(reverse('auth:login'))
        else:
            pass
    else:
        register_form = ShopUserLogoutForm()

    content = {'title': title, 'register_form': register_form}
    return render(request, 'authnapp/register.html', content)

def logout(request):
    info_index = {
        'index_heading': 'geekShop store',
        'index_welcome_text': 'новые образы и лучшие бренды на GeekShop Store. бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'index_start_purchase': 'начать покупки'
    }

    auth.logout(request)
    return render(request, 'product/index.html', info_index)