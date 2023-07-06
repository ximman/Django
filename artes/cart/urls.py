from .views import *
from django.urls import path

app_name='cart'
urlpatterns=[
    path('', cart_detail, name='cart_detail'),
    path('add/<int:product_id>/<change>/', add_cart, name='add_cart'),
    path('remove/<int:product_id>/', cart_remove, name='cart_remove'),
    path('clear/', cart_clear, name='cart_clear')
]