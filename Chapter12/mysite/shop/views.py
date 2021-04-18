from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Product
from cart.forms import CartAddProductForm

def myview(request):
    print(request.user)
    print(request.session)
    return HttpResponse("커맨드창을 확인하세요")

def product_list(request):
    products = Product.objects.filter(available=True)
    return render(request, 'product/list.html', {'products': products})

def product_detail(request, id):
    product = get_object_or_404(Product, id=id, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'product/detail.html', {'product': product, 'cart_product_form': cart_product_form})