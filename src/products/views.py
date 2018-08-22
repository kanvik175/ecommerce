from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Category

class ProductListView(ListView):
    template_name = "products/list.html"
    model = Product
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    model = Product
    template_name = "products/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
