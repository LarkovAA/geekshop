from django.contrib.auth.decorators import user_passes_test
from django.db import connection
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, UpdateView, CreateView, DeleteView, DetailView

from admins.forms import UserAdminRegisterForm, UserAdminProfilForm, CategoryAdminRegisterForm, CategoryAdminUpdateForm, \
    ProductAdminRegisterForm, ProductAdminUpdateForm
from authnapp.models import ShopUser
from product.models import Category, Product

def db_profile_by_type(prefix, type, queries):
    update_queries = list(filter(lambda x: type in x['sql'], queries))
    print((f'db_profile {type} for {prefix}:'))
    [print(query['sql']) for query in update_queries]


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')

class UserListView(ListView):
    model = ShopUser
    template_name = 'admins/admin-users-read.html'
    context_object_name = 'shop_users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = "Админка | Пользователи"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserListView,self).dispatch(request, *args, **kwargs)

class UserCreateView(CreateView):
    model = ShopUser
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = "Админка | Создать пользователя"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserCreateView,self).dispatch(request, *args, **kwargs)

class UserUpdateView(UpdateView):
    model = ShopUser
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfilForm
    success_url = reverse_lazy('admins:admin_users')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Админка | Обновить пользователя"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

class UserDeleteView(DeleteView):
    model = ShopUser
    template_name = 'admins/admin-users-update-delete.html'
    # form_class = UserAdminProfilForm
    success_url = reverse_lazy('admins:admin_users')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Админка | Удалить пользователя"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

class CategoryListView(ListView):
    model = Category
    template_name = 'admins/admin_category.html'
    context_object_name = 'categoryes'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = "Категории"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryListView,self).dispatch(request, *args, **kwargs)

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'admins/admin_category_create.html'
    form_class = CategoryAdminRegisterForm
    success_url = reverse_lazy('admins:admin_category_create')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = "Админка | Создать пользователя"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryCreateView,self).dispatch(request, *args, **kwargs)

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = 'admins/admin_categoryes_update_delete.html'
    form_class = CategoryAdminUpdateForm
    success_url = reverse_lazy('admins:admin_category')

    def form_valid(self, form):
        if 'discount' in form.cleaned_data:
            discount = form.cleaned_data['discount']
            if discount:
                print(f'применяется скидка {discount} % к товарам категории {self.object.name}')
                self.object.product_set.update(price=F('price')*(1-discount/100))
                db_profile_by_type(self.__class__,'UPDATE', connection.queries)
        return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Админка | Обновить пользователя"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(CategoryUpdateView, self).dispatch(request, *args, **kwargs)

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'admins/admin-users-update-delete.html'
    # form_class = UserAdminProfilForm
    success_url = reverse_lazy('admins:admin_category')

    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.is_active = False
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Админка | Удалить пользователя"
        return context

class ProductListView(ListView):
    model = Product
    template_name = 'admins/admin_product.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = "Продукты"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductListView,self).dispatch(request, *args, **kwargs)


class ProductCreateView(CreateView):
    model = Product
    template_name = 'admins/admin_product_create.html'
    form_class = ProductAdminRegisterForm
    success_url = reverse_lazy('admins:admin_product_create')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductCreateView, self).get_context_data(**kwargs)
        context['title'] = "Админка | Создать новый продукт"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductCreateView,self).dispatch(request, *args, **kwargs)

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'admins/admin_product_update_delete.html'
    form_class = ProductAdminUpdateForm
    success_url = reverse_lazy('admins:admin_product')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = "Админка | Обновить информацио о продукте"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductUpdateView, self).dispatch(request, *args, **kwargs)

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'admins/admin_product_update_delete.html'
    # form_class = UserAdminProfilForm
    success_url = reverse_lazy('admins:admin_product')
    #
    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     self.object.is_active = False
    #     self.object.save()
    #     return HttpResponseRedirect(self.get_success_url())

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDeleteView, self).get_context_data(**kwargs)
        context['title'] = "Админка | Удалить пользователя"
        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(ProductDeleteView, self).dispatch(request, *args, **kwargs)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, name):
    if request.method == 'POST':
        user = Product.objects.get(name=name)
        user.is_active = False
        user.save()

    return HttpResponseRedirect(reverse('admins:admin_product'))

