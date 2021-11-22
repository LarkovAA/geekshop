from django.urls import path

from authnapp import views
import product.views as product

app_name = 'authnapp'

urlpatterns = [
   path('', views.login, name='login'),
   path('register', views.register, name='register'),
]
