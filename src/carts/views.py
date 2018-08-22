from django.shortcuts import render

from carts.models import Cart

def cart_create(user = None):
    cart_obj = Cart.objects.create(user = None)
    print("New cart created")
    return cart_obj

def cart_home(request):
    cart_id = request.session.get("cart_id", None)
    # if cart_id is None and isinstance(cart_id, int):
    #     cart_obj = cart_create()
    #     request.session['cart_id'] = cart_obj.id
    #     print("New cart is created")
    # else:
    qs = Cart.objects.filter(id = cart_id)
    if qs.count() == 1:
        cart_obj = qs.first()
        print("Cart ID exists")
    else:
        cart_obj = cart_create()
        requset.session["cart_id"] = cart_obj.id
    return render(request, "carts/home.html", {})
