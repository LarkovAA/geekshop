from django.core.management import BaseCommand

from product.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        from django.db.models import Q
        product = Product.objects.filter(Q(category__name='Обувь') | Q(id=4))
        print(product)