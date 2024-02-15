from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from .cart import Cart
from shop.models import Product




def cart_summry(request):
    return render(request, 'cart_summry.html')

def cart_add(request):
    cart = Cart(request)

    if request.POST.get('action')=='post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product)

        cart_quantity = cart.__len__()
        # response = JsonResponse({'Product name': product.name})
        response = JsonResponse({'qty': cart_quantity})

        return response

def cart_delete(request):
    pass

def cart_update(request):
    pass
