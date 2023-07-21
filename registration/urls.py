from django.contrib.auth.views import LogoutView
from django.urls import path

from core import settings
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]
