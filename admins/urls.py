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
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

