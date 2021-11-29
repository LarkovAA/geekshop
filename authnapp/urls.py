from django.urls import path
from authnapp import views


app_name = 'auth'

urlpatterns = [
   path('login/', views.login, name='login'),
   path('register/', views.register, name='register'),
   path('logout/', views.logout, name='logout'),
   path('profile/', views.profile, name='profile'),
]

