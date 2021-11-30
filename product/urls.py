from django.urls import path

from product import views
import product.views as product

app_name = 'products'

urlpatterns = [
   path('', views.products, name='index'),
]
