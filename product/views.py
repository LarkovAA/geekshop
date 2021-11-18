from django.shortcuts import render

# Create your views here.
def index(request):
    info_index = {
        'index_heading': 'geekShop store',
        'index_welcome_text': 'новые образы и лучшие бренды на GeekShop Store. бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.',
        'index_start_purchase': 'начать покупки'
    }
    return render(request, 'index.html', context=info_index)

def products(request):
    info_products = {
        'list_products': [
            {
            'name': 'Худи черного цвета с монограммами adidas Originals',
            'price': 6090.00,
            'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
            'img': 'vendor/img/products/Adidas-hoodie.png'
            },
            {
                'name': 'Синяя куртка The North Face',
                'price': 23725.00,
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'img': 'vendor/img/products/Blue-jacket-The-North-Face.png'
            },
            {
                'name': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'price': 3390.00,
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'img': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png'
            },
            {
                'name': 'Черный рюкзак Nike Heritage',
                'price': 2340.00,
                'description': 'Плотная ткань. Легкий материал.',
                'img': 'vendor/img/products/Black-Nike-Heritage-backpack.png'
            },
            {
                'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'price': 13590.00,
                'description': 'Гладкий кожаный верх. Натуральный материал.',
                'img': 'vendor/img/products/Black-Dr-Martens-shoes.png'
            },
            {
                'name': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'price': 2890.00,
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                'img': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png'

            },
    ],
        'products_heading': 'GeekShop - Каталог'
    }
    return render(request, 'products.html', context=info_products)