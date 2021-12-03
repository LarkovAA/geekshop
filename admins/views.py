from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from admins.forms import UserAdminRegisterForm, UserAdminProfilForm, CategoryAdminRegisterForm, CategoryAdminUpdateForm, \
    ProductAdminRegisterForm, ProductAdminUpdateForm
from authnapp.models import ShopUser
from product.models import Category, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')

@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'shop_users': ShopUser.objects.all(),
        'title': 'Пользователи'
    }
    return render(request, 'admins/admin-users-read.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_user_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))

    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Geekshop - Админ | Регистрация',
        'form': form,
    }
    return render(request, 'admins/admin-users-create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_user_update(request, pk):

    user_select = ShopUser.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserAdminProfilForm(data=request.POST, files=request.FILES, instance=user_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))

    else:
        form = UserAdminRegisterForm(instance=user_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form': form,
        'user_select': user_select,
    }
    return render(request, 'admins/admin-users-update-delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_user_delete(request, pk):
    if request.method == 'POST':
        user = ShopUser.objects.get(pk=pk)
        user.is_active = False
        user.save()

    return HttpResponseRedirect(reverse('admins:admin_users'))

@user_passes_test(lambda u: u.is_superuser)
def admin_category(request):
    context = {
        'categoryes': Category.objects.all(),
        'title': 'Категории'
    }
    return render(request, 'admins/admin_category.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category_create'))

    else:
        form = CategoryAdminRegisterForm()
    context = {
        'title': 'Geekshop - Админ | Создание новой категории',
        'form': form,
    }
    return render(request, 'admins/admin_category_create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_categoryes_update(request,id):
    categoty_select = Category.objects.get(id=id)

    if request.method == 'POST':
        form = CategoryAdminUpdateForm(data=request.POST, files=request.FILES, instance=categoty_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_category'))

    else:
        form = CategoryAdminUpdateForm(instance=categoty_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form': form,
        'categoty_select': categoty_select,
    }
    return render(request, 'admins/admin_categoryes_update_delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_categoryes_delete(request, id):
    if request.method == 'POST':
        user = Category.objects.get(id=id)
        user.is_active = False
        user.save()

    return HttpResponseRedirect(reverse('admins:admin_category'))

@user_passes_test(lambda u: u.is_superuser)
def admin_product(request):
    context = {
        'products': Product.objects.all(),
        'title': 'Категории'
    }
    return render(request, 'admins/admin_product.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_create(request):
    if request.method == 'POST':
        form = ProductAdminRegisterForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product_create'))

    else:
        form = ProductAdminRegisterForm()
    context = {
        'title': 'Geekshop - Админ | Создание нового продукта',
        'form': form,
    }
    return render(request, 'admins/admin_product_create.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_update(request,name):
    product_select = Product.objects.get(name=name)

    if request.method == 'POST':
        form = ProductAdminUpdateForm(data=request.POST, files=request.FILES, instance=product_select)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_product'))

    else:
        form = ProductAdminUpdateForm(instance=product_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form': form,
        'product_select': product_select,
    }
    return render(request, 'admins/admin_product_update_delete.html', context)

@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, name):
    if request.method == 'POST':
        user = Product.objects.get(name=name)
        user.is_active = False
        user.save()

    return HttpResponseRedirect(reverse('admins:admin_product'))

