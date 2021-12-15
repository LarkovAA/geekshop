from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from admins import views
from admins.views import UserListView, UserCreateView, UserUpdateView, UserDeleteView, CategoryListView, \
    CategoryCreateView, CategoryUpdateView, CategoryDeleteView, ProductListView, ProductCreateView, ProductUpdateView, \
    ProductDeleteView

app_name = 'admins'

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', UserListView.as_view(), name='admin_users'),
    path('user_update/<int:pk>', UserUpdateView.as_view(), name='admin_user_update'),
    path('user_create/', UserCreateView.as_view(), name='admin_user_create'),
    path('user_delete/<int:pk>', UserDeleteView.as_view(), name='admin_user_delete'),
    path('admin_category/', CategoryListView.as_view(), name='admin_category'),
    path('admin_category_create/', CategoryCreateView.as_view(), name='admin_category_create'),
    path('admin_categoryes_update/<int:pk>', CategoryUpdateView.as_view(), name='admin_categoryes_update'),
    path('admin_categoryes_delete/<int:pk>', CategoryDeleteView.as_view(), name='admin_categoryes_delete'),
    path('admin_product/', ProductListView.as_view(), name='admin_product'),
    path('admin_product_create/', ProductCreateView.as_view(), name='admin_product_create'),
    path('admin_product_update/<int:pk>', ProductUpdateView.as_view(), name='admin_product_update'),
    path('admin_product_delete/<int:pk>', ProductDeleteView.as_view(), name='admin_product_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

