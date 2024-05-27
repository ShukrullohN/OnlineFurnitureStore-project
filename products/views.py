from django.shortcuts import render
from products.models import ProductModel
from django.views.generic import TemplateView, ListView
class ProductListView(ListView):
    template_name= "products/product-list.html"
    model = ProductModel
    context_object_name = 'products'