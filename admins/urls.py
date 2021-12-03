from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from admins import views

app_name = 'admins'

urlpatterns = [
    path('', views.index, name='index'),
    path('users/', views.admin_users, name='admin_users'),
    path('user_update/<int:pk>', views.admin_user_update, name='admin_user_update'),
    path('user_create/', views.admin_user_create, name='admin_user_create'),
    path('user_delete/<int:pk>', views.admin_user_delete, name='admin_user_delete'),
    path('admin_category/', views.admin_category, name='admin_category'),
    path('admin_category_create/', views.admin_category_create, name='admin_category_create'),
    path('admin_categoryes_update/<int:id>', views.admin_categoryes_update, name='admin_categoryes_update'),
    path('admin_categoryes_delete/<int:id>', views.admin_categoryes_delete, name='admin_categoryes_delete'),
    path('admin_product/', views.admin_product, name='admin_product'),
    path('admin_product_create/', views.admin_product_create, name='admin_product_create'),
    path('admin_product_update/<str:name>', views.admin_product_update, name='admin_product_update'),
    path('admin_product_delete/<str:name>', views.admin_product_delete, name='admin_product_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

