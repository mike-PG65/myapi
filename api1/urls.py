# urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('users/', views.get_users, name='get_user'),
    path('users/create/', views.create_user, name='create_user'),
]
