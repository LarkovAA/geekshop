from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from authnapp import views
from authnapp.views import RegUserCreateView

app_name = 'auth'

urlpatterns = [
   path('login/', views.login, name='login'),
   path('register/', RegUserCreateView.as_view(), name='register'),
   path('logout/', views.logout, name='logout'),
   path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
