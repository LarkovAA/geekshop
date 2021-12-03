from django.urls import path

from product import views
import product.views as product

app_name = 'products'

urlpatterns = [
   path('', views.products, name='index'),
   path('detail/<int:pk>/', product.ProductDetail.as_view(), name='detail'),
]
