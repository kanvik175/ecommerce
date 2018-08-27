from django.shortcuts import render, redirect

from products.models import Product
from carts.models import Cart

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for item in products:
        total += item.price
    cart_obj.total = total
    cart_obj.save()
    context = {"cart" : cart_obj}
    print(cart_obj.products)
    return render(request, "carts/home.html", context)

def cart_update(request):
    print(request.POST)
    product_id = request.POST.get("product_id")
    if product_id is not None:
        try:
            product_obj = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return redirect("list")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj not in cart_obj.products.all():
            cart_obj.products.add(product_obj)
        else:
            cart_obj.products.remove(product_obj)
        cart_obj.save()
    return redirect("cart:home")
