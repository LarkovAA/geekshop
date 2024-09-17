from django.core.management.base import BaseCommand
from product.models import Category, Product
from django.contrib.auth.models import User
from authnapp.models import ShopUser

import json, os

JSON_PATH = 'product/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('category')

        Category.objects.all().delete()
        for cat_ry in categories:
            ner_category = Category(id=cat_ry['id'], name=cat_ry['name'], description=cat_ry['description'])
            ner_category.save()

        products = load_from_json('product')
        Product.objects.all().delete()
        for product in products:
            category_name = product['category']
            _category = Category.objects.get(name=category_name)
            product['category'] = _category
            new_product = Product(id=product['id'], name=product['name'], image=product['image'], short_desc=product['short_desc'],
                                  description=product['description'], price=product['price'], quantity=product['quantity'], category=product['category'],)
            new_product.save()

        super_user = ShopUser.objects.create_superuser(
            'kane93', 'lexlar@mail.ru', 'lexa2454811@', age=28)
