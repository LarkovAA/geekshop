from django.urls import path

from authnapp import views
import product.views as product

app_name = 'authnapp'

urlpatterns = [
   path('login/', views.login, name='login'),
   path('logout/', views.logout, name='logout'),
]
