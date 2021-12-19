from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from authnapp.views import RegUserCreateView, LoginLoginView, ProfileUpdateView, Logout

app_name = 'auth'

urlpatterns = [
    path('login/', LoginLoginView.as_view(), name='login'),
    path('register/', RegUserCreateView.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('profile/', ProfileUpdateView.as_view(), name='profile'),
    path('verify/<str:email>/<str:activation_key>/', RegUserCreateView.verify, name='verify'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
