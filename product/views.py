from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import DetailView

from .models import Category, Product
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
        products_bd = Product.objects.filter(category=id_category)
    else:
        products_bd = Product.objects.all()

    paginator = Paginator(products_bd, per_page=2)

    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    category_bd = Category.objects.all()
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
        product = self.get_object()
        context['product'] = product
        return context

