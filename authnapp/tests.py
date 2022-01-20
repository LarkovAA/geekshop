from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from django.conf import settings

# Create your tests here.


class UserManagementTestSase(TestCase):
    username = 'django'
    email = 'django@mail.ru'
    password = 'geekshop'

    new_user_data = {
        'username':'django1',
        'first_name': 'django11',
        'last_name': 'django111',
        'password1':'Isponec_2',
        'password2': 'Isponec_2',
        'email': 'geekshop@mail.ru',
        'age': 28,
    }

    def setUp(self):
        self.user = User.objects.create_superuser(self.username, email=self.email, password=self.password)
        self.client = Client()

    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

        self.assertTrue(response.context['user'].is_anonymous)

        self.client.login(username=self.username, password=self.password)

        response = self.client.get('/auth/login/')

        self.assertEqual(response.status_code, 302)

    def test_register(self):
        response = self.client.post('/auth/register/', data=self.new_user_data)
        print(response.status_code)

        self.assertTrue(response.status_code, 302)

        new_user = User.objects.get(username=self.new_user_data['username'])
        activation_url = f'{settings.DOMAIN_NAME}/users/verify/{self.new_user_data["email"]}/{new_user.activation_key}'

        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, 302 )

        new_user.refresh_from_db()
        self.assertTrue(new_user.is_active)

    def tearDown(self):
        pass


