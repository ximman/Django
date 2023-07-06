from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm

menu = [{'title':'Вход', 'url_name':'shop:login'},
        {'title':'Регистрация', 'url_name':'shop:register'},
        {'title':'Категории товаров', 'url_name':'shop:category'},
        {'title':'Товары', 'url_name':'shop:product'},
        {'title':'Корзина', 'url_name':'cart:cart_detail'},
]
def add_cart(request, product_id, change):
    cart=Cart(request)
    product=get_object_or_404(Product, id=product_id)
    form=CartAddProductForm(request.POST)
    if str(product_id) in cart.cart.keys() and change!=0:
        cart.cart[str(product_id)]['quantity']+=int(change)
        cart.save()
    if form.is_valid():
        cd=form.cleaned_data
        cart.add(
            product=product,
            quantity=cd['quantity'],
            update_quantity=cd['update']
        )
    return redirect('cart:cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')

def cart_detail(request):
    cart = Cart(request)
    if not request.user.is_authenticated:
        return redirect('shop:product')
    return render(request, 'details.html', {'cart': cart, 'title':'Корзина', 'menu':menu})

def cart_clear(request):
    cart=Cart(request)
    cart.clear()
    return redirect('cart:cart_detail')
