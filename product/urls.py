from django.urls import path

from product import views
import product.views as product

app_name = 'products'

urlpatterns = [
   path('', views.products, name='index'),
   path('category/<int:id_category>', views.products, name='category'),
   path('page/<int:page>', views.products, name='page'),
   path('detail/<int:pk>/', product.ProductDetail.as_view(), name='detail'),
]
