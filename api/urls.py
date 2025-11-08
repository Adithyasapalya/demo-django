from django.urls import path
from . import views
from .views import get_users, create_users

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', views.create_users, name='create_users'),
    path('users/<int:pk>', views.create_users, name='create_users')
]