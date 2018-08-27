from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Category


class ProductListView(ListView):
    template_name = "products/list.html"
    queryset = Product.objects.all()
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        print("list")
        from carts.models import Cart
        request = self.request
        context = super().get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['categories'] = Category.objects.all()
        context['cart'] = cart_obj
        return context


class ProductDetailView(DetailView):

    template_name = "products/detail.html"

    def get_context_data(self, *args, **kwargs):
        print("detail")
        from carts.models import Cart
        request = self.request
        context = super().get_context_data(*args, **kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        context['categories'] = Category.objects.all()
        context['cart'] = cart_obj
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        instance = Product.objects.get(slug = slug)
        if instance is None:
            raise Http404("Product doesn't exist")
        return instance
