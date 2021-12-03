from django.shortcuts import render
from django.views.generic import DetailView

from .models import Category, Product
# Create your views here.
def index(request):
    info_index = {
        'index_heading': 'geekShop store',
        'index_welcome_text': 'новые образы и лучшие бренды на GeekShop Store. бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'index_start_purchase': 'начать покупки'
    }
    return render(request, 'index.html', context=info_index)

def products(request):
    products_bd = Product.objects.all()
    category_bd = Category.objects.all()

    info_products = {
        'list_products': products_bd,
        'list_categoty': category_bd,
        'products_heading': 'GeekShop - Каталог',
    }
    return render(request, 'products.html', context=info_products)

class ProductDetail(DetailView):
    model = Product
    template_name = 'product/detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetail, self).get_context_data(**kwargs)
        product = self.get_object()
        context['product'] = product
        return context

