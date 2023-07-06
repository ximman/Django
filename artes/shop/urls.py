from django.urls import path
from .views import *
from rest_framework.authtoken import views

app_name='shop'
urlpatterns = [
    path('category/', category, name='category'),
    path('product/', product, name='product'),
    path('login/', log_in, name='login'),
    path('token_login/', token_login, name='tokenlogin'),
    path('logout', log_out, name='logout'),
    path('register/', register, name='register')
]