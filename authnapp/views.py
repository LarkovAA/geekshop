from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.views import LoginView, LogoutView
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from authnapp.forms import ShopUserLoginForm, ShopUserRegistrtForm, ShopUserProfilForm
from django.contrib import auth, messages
from django.urls import reverse, reverse_lazy

# Create your views here.
from authnapp.models import ShopUser
from baskets.models import Basket
from mixin import BaseClassContexMixin, UserDispatchMixin

# def login(request):
#     title = 'Ввод данных'
#     if request.method == 'POST':
#         login_form = ShopUserLoginForm(data=request.POST)
#         if login_form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#
#                 return HttpResponseRedirect(reverse('index'))
#         else:
#             print(login_form.errors)
#     else:
#         login_form = ShopUserLoginForm()
#
#     content = {'title': title, 'login_form': login_form}
#     return render(request, 'authnapp/login.html', content)

class LoginLoginView(LoginView, BaseClassContexMixin):
    template_name = 'authnapp/login.html'
    form_class = ShopUserLoginForm
    redirect_authenticated_user = reverse_lazy('auth:profile')
    title = 'Ввод данных'

class RegUserCreateView(CreateView):
    model = ShopUser
    template_name = 'authnapp/register.html'
    form_class = ShopUserRegistrtForm
    success_url = reverse_lazy('auth:login')

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            user = form.save()
            if self.send_verify_link(user):
                messages.set_level(request, messages.SUCCESS)
                messages.success(request, 'Вы успешно зарегистрировались')
                return HttpResponseRedirect(reverse('auth:login'))
            else:
                messages.set_level(request, messages.ERROR)
                messages.error(request, form.errors)

        else:
            messages.set_level(request, messages.ERROR)
            messages.error(request, form.errors)
        return render(request, self.template_name, {'form': form})

    def send_verify_link(self, user):
        verify_link = reverse('auth:verify', args=[user.email, user.activation_key])
        subject = f'Для активации учетной записи {user.username} пройтите по ссылке'
        messages = f'Для подтверждения учетной записи {user.username} на портале \n {settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, messages, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

    def verify(self, email, activation_key):
        try:
            user = ShopUser.objects.get(email=email)
            if user and user.activation_key == activation_key and not user.is_activation_key_expires():
                user.activation_key = ''
                user.activation_key_expires = None
                user.is_active = True
                user.save()
                auth.login(self, user)
            return render(self, 'authnapp/verification.html')
        except Exception as e:
            return HttpResponseRedirect(reverse('index'))

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

class ProfileUpdateView(UpdateView, UserDispatchMixin):
    template_name = 'authnapp/profile.html'
    form_class = ShopUserProfilForm
    success_url = reverse_lazy('auth:profile')
    title = 'Профайл'

    def form_valid(self, form):
        messages.set_level(self.request, messages.SUCCESS)
        messages.success(self.request, "Вы успешно зарегистрировались")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, *args, **kwargs):
        return get_object_or_404(ShopUser, pk=self.request.user.pk)

    # def get_context_data(self, **kwargs):
    #     context = super(ProfileUpdateView, self).get_context_data(**kwargs)
    #     context['baskets'] = Basket.objects.filter(user=self.request.user)
    #     return context

# @login_required
# def profile(request):
#     title = 'Профайл'
#     if request.method == 'POST':
#         profile_form = ShopUserProfilForm(instance=request.user, data=request.POST, files=request.FILES)
#         if profile_form.is_valid():
#             messages.success(request, 'Вы успешно сохранили профайл.')
#             profile_form.save()
#         else:
#             print(profile_form.errors)
#
#     baskets = Basket.objects.filter(user=request.user)
#     # summ = (basket.quantity * basket.product.price for basket in baskets)
#     total_sum = sum(basket.summ() for basket in baskets)
#     total_quantity = sum(basket.quantity for basket in baskets)
#
#     content = {
#         'title': title,
#         'profile_form': ShopUserProfilForm(instance=request.user),
#         'baskets': baskets,
#         'total_quantity': total_quantity,
#         'total_sum': total_sum,
#         # 'summ': summ
#
#     }
#     return render(request, 'authnapp/profile.html', content)

class Logout(LogoutView):
    template_name = 'product/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(Logout, self).get_context_data(**kwargs)
        context['index_heading'] = 'geekShop store'
        context['index_welcome_text'] = 'новые образы и лучшие бренды на GeekShop Store. бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
        context['index_start_purchase'] = 'начать покупки'
        return context

