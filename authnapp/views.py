from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from authnapp.forms import ShopUserLoginForm, ShopUserRegistrtForm, ShopUserProfilForm
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy

# Create your views here.
from authnapp.models import ShopUser
from baskets.models import Basket

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
            print(login_form.errors)
    else:
        login_form = ShopUserLoginForm()

    content = {'title': title, 'login_form': login_form}
    return render(request, 'authnapp/login.html', content)

class RegUserCreateView(CreateView):
    model = ShopUser
    template_name = 'authnapp/register.html'
    form_class = ShopUserRegistrtForm
    success_url = reverse_lazy('auth:login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(RegUserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Регистрация'
        return context

    def dispatch(self, request, *args, **kwargs):
        return super(RegUserCreateView,self).dispatch(request, *args, **kwargs)

# def register(request):
#     title = 'Регистрация'
#
#     if request.method == 'POST':
#         register_form = ShopUserRegistrtForm(data=request.POST)
#         if register_form.is_valid():
#             register_form.save()
#             messages.success(request, 'Вы успешно зарегистрировалиcь.')
#             return HttpResponseRedirect(reverse('auth:login'))
#     else:
#         register_form = ShopUserRegistrtForm()
#
#     content = {'title': title, 'register_form': register_form}
#     return render(request, 'authnapp/register.html', content)

@login_required
def profile(request):
    title = 'Профайл'
    if request.method == 'POST':
        profile_form = ShopUserProfilForm(instance=request.user, data=request.POST, files=request.FILES)
        if profile_form.is_valid():
            messages.success(request, 'Вы успешно сохранили профайл.')
            profile_form.save()
        else:
            print(profile_form.errors)

    baskets = Basket.objects.filter(user=request.user)
    # summ = (basket.quantity * basket.product.price for basket in baskets)
    total_sum = sum(basket.summ() for basket in baskets)
    total_quantity = sum(basket.quantity for basket in baskets)

    content = {
        'title': title,
        'profile_form': ShopUserProfilForm(instance=request.user),
        'baskets': baskets,
        'total_quantity': total_quantity,
        'total_sum': total_sum,
        # 'summ': summ

    }
    return render(request, 'authnapp/profile.html', content)

def logout(request):
    info_index = {
        'index_heading': 'geekShop store',
        'index_welcome_text': 'новые образы и лучшие бренды на GeekShop Store. бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'index_start_purchase': 'начать покупки'
    }
    auth.logout(request)
    return render(request, 'product/index.html', info_index)

