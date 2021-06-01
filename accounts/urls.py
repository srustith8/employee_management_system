from django.urls import path
from accounts import views

urlpatterns = [
    path("register/", views.register, name='register'),
    path("login/", views.login, name='login'),
    path("logout/", views.logout, name='logout'),
    path("register/login/", views.login, name='login'),
    path("profile/", views.profile, name='profile'),
    path('change_password/', views.change_password, name='change_password'),
  
]
