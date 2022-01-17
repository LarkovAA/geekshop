from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Category, Product
from django.conf import settings
from django.core.cache import cache

def get_link_product():
    if settings.LOW_CACHE:
        key = 'link_product'
        link_product = cache.get(key)
        if link_product is None:
            link_product = Product.objects.all().select_related('category')
            cache.set(key, link_product)
        return link_product
    else:
        return Product.objects.all().select_related('category')

def get_link_category():
    if settings.LOW_CACHE:
        key = 'link_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = Category.objects.all()
            cache.set(key, link_category)
        return link_category
    else:
        return Category.objects.all()

def get_product(pk):
    if settings.LOW_CACHE:
        key = f'product{pk}'
        product = cache.get(key)
        if product is None:
            product = Product.objects.get(id=pk)
            cache.set(key, product)
        return product
    else:
        return Product.objects.get(id=pk)

# Create your views here.
def index(request):
    info_index = {
        'index_heading': 'geekShop store',
        'index_welcome_text': 'новые образы и лучшие бренды на GeekShop Store. бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'index_start_purchase': 'начать покупки',
    }
    return render(request, 'product/index.html', info_index)


def products(request, id_category=None, page=1):
    if id_category:
        products_bd = Product.objects.filter(category=id_category).select_related('category')
    else:
        products_bd = Product.objects.all().select_related('category')

    products_bd = get_link_product()

    paginator = Paginator(products_bd, per_page=2)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    # category_bd = Category.objects.all()
    category_bd = get_link_category()
    products_bd = products_paginator
    info_products = {
        'list_products': products_bd,
        'list_categoty': category_bd,
        'products_heading': 'GeekShop - Каталог',
    }

    return render(request, 'product/products.html', info_products)

class ProductDetail(DetailView):
    model = Product
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        context['product'] = get_product(self.kwargs.get('pk'))
        return context

