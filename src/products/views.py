from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product

class ProductListView(ListView):
    template_name = "products/list.html"
    model = Product
    queryset = Product.objects.all()
    paginate_by = 1

class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    model = Product
    template_name = "products/detail.html"
