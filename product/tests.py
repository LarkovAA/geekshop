from django.test import TestCase, Client
from product.models import Product, Category
# Create your tests here.

class TestMainSmokeTest(TestCase):

    def setUp(self):
        category = Category.objects.create(
            name='TestCat1'
        )
        Product.objects.create(
            category=category,
            name='product_test_1',
            price=100
        )
        self.client = Client()
    def tearDown(self):
        pass

    def test_products_pages(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,200)

    def test_products_product(self):
        for product_items in Product.objects.all():
            response = self.client.get(f'/products/detail/{product_items.pk}')
            self.assertEqual(response.status_code, 200)