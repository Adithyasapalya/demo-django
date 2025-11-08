# basic django rest api demo project
# i did basic django frest framework api project with create, read, update, delete operations
# and also added serializer for model serialization

from django.urls import path
from . import views
from .views import get_users, create_users, user_detail

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/',create_users, name='create_users'),
    path('users/<int:pk>',user_detail, name='user_detail')
] 