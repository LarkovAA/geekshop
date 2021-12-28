from django.conf import settings
from django.conf.urls.static import static
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

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
