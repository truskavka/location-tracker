from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('registration/', views.RegistrationView.as_view(), name='registration'),
    # path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
]
