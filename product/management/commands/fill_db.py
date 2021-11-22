from django.core.management.base import BaseCommand
from product.models import Category, Product
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'product/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('categoty')

        Category.objects.all().delete()
        for cat_ry in categories:
            ner_category = Product(**cat_ry)
            ner_category.save()

        products = load_from_json('product')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = Category.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(**product)
            new_product.save()

        super_user = User.objects.create_superuser(
            'kane93', 'lexlar@mail.ru', 'lexa2454811@'
        )
