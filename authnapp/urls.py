from django.urls import path

from authnapp import views
import product.views as product

app_name = 'auth'

urlpatterns = [
   path('login/', views.login, name='login'),
   path('register/', views.register, name='register'),
   path('logout/', views.logout, name='logout'),
]
