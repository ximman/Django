from time import sleep

from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import RequestContext
from django.urls import reverse_lazy

from .forms import *
from .models import *
from cart.forms import CartAddProductForm
from django.contrib.auth.models import User

menu = [{'title':'Вход', 'url_name':'shop:login'},
        {'title':'Регистрация', 'url_name':'shop:register'},
        {'title':'Категории товаров', 'url_name':'shop:category'},
        {'title':'Товары', 'url_name':'shop:product'},
        {'title':'Корзина', 'url_name':'cart:cart_detail'},
]
def category(request):
    cat_list=Category.objects.all()
    subcat_list=Subcategory.objects.all()
    paginator=Paginator(cat_list, 3)
    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)
    return render(
        request,
        'category.html',
        {'title':'Список категорий',
         'subcat_list':subcat_list,
         'page_obj':page_obj,
         'menu':menu
         }
    )

def product(request):
    product_list=Product.objects.all()
    paginator=Paginator(product_list, 3)
    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)
    cart_add_form=CartAddProductForm
    return render(
        request,
        'product.html',
        {'title':'Список товаров',
         'product_list':product_list,
         'page_obj':page_obj,
         'cart_add_form':cart_add_form,
         'menu': menu,
         'is_auth':request.user.is_authenticated
         }
    )

def register(request):
    form=RegisterForm(data=request.POST)
    if form.is_valid():
        User.objects.create_user(
            username=form.cleaned_data['username'],
            email=form.cleaned_data['username']+'@mail.ru',
            password=form.cleaned_data['password1'],
        )
        return redirect('shop:login')
    return render(
        request,
        'register.html',
        {'title':'Регистрация',
         'form':form,
         'menu':menu
        }
    )

def log_in(request):
    form=LoginForm(data=request.POST)
    print('form.is_valid:', form.is_valid())
    if form.is_valid():
        user=authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
        login(request, user)
    return render(
        request,
        'login.html',
        {
            'title':'Вход',
            'form':form,
            'menu':menu

        },
    )

def log_out(request):
    print(request.user.is_authenticated)
    logout(request)
    print(request.user.is_authenticated)
    return redirect('shop:login')

def token_login(request):
    return HttpResponse('Authorization: Token 7000a2ebdef80859cf59c3553f55de71a30a6dae')