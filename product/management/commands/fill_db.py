from django.core.management.base import BaseCommand
from product.models import Category, Product
from django.contrib.auth.models import User

import json, os

JSON_PATH = 'product/json'

def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name + '.json'), 'r') as infile:
        return json.load(infile)

class Command(BaseCommand):
    pass