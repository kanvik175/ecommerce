from django.http import HttpResponse
from django.shortcuts import render, redirect

def home_page(request):
    print(request.session.get('cart_product', 'unknown'))
    return render(request, "home_page.html")
