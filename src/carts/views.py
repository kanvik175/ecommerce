from django.shortcuts import render, redirect

from orders.models import Order
from products.models import Product
from carts.models import Cart
from accounts.forms import LoginForm, GuestForm
from accounts.models import GuestEmail
from billing.models import BillingProfile

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

def checkout_home(request):
    cart_obj, cart_created = Cart.objects.new_or_get(request)
    if cart_created or cart_obj.products.count() == 0:
        return redirect("cart:home")
    else:
        order_obj, new_order_obj = Order.objects.get_or_create(cart=cart_obj)
    user = request.user
    login_form = LoginForm()
    guest_form = GuestForm()
    guest_email_id = request.session.get("guest_email_id")
    billing_profile = None
    if user.is_authenticated():
        billing_profile, billing_profile_created=BillingProfile.objects.get_or_create(user=user, email=user.email)
    elif guest_email_id is not None:
        guest_email_obj = GuestEmail.objects.get(id=guest_email_id)
        billing_profile, billing_guest_profile_created = BillingProfile.objects.get_or_create(
                                                email=guest_email_obj.email
        )
    else:
        pass

    print("Billing profile")
    print(billing_profile)
    context = {
        "object" : order_obj,
        "billing_profile" : billing_profile,
        "login_form" : login_form,
        "guest_form" : guest_form
    }


    return render(request, "carts/checkout.html", context)
