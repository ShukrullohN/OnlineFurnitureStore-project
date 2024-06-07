from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView

from products.models import ProductModel, ProductCategoryModel, ProductColorModel, ProductTagModel, ProductManufacture, \
    ProductImageModel


class ProductsListView(ListView):
    template_name = 'products/product-list.html'
    model = ProductModel
    context_object_name = 'products'

    @staticmethod
    def change_colors_structure():
        colors = ProductColorModel.objects.all()
        colors_list = []
        temp_colors = []

        for color in colors:
            temp_colors.append(color)
            if len(temp_colors) == 2:
                colors_list.append(temp_colors)
                temp_colors = []  # Reset temp_colors to a new list after appending

        # Append any remaining colors in temp_colors if it is not empty
        if temp_colors:
            colors_list.append(temp_colors)

        return colors_list

    def get_queryset(self):
        products = self.model.objects.all().order_by('-created_at')
        tag = self.request.GET.get('tag')
        cat = self.request.GET.get('cat')
        col = self.request.GET.get('col')
        man = self.request.GET.get('man')
        sort = self.request.GET.get('sort')
        q = self.request.GET.get('q')

        if tag:
            products = products.filter(tags__in=tag)
        if cat:
            products = products.filter(categories__in=cat)
        if col:
            products = products.filter(colors__in=col)
        if man:
            products = products.filter(manufacture__in=man)
        if sort:
            if sort == '-price':
                products = products.order_by('-real_price')
            else:
                products = products.order_by('real_price')
        if q:
            products = products.filter(name__icontains=q)

        return products

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = ProductCategoryModel.objects.all()
        context['manufactures'] = ProductManufacture.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['colors'] = ProductColorModel.objects.all()
        return context


class ProductDetailView(DetailView):
    template_name = 'products/product-detail.html'
    model = ProductModel

    @staticmethod
    def change_colors_structure():
        colors = ProductColorModel.objects.all()
        colors_list = []
        temp_colors = []

        for color in colors:
            temp_colors.append(color)
            if len(temp_colors) == 2:
                colors_list.append(temp_colors)
                temp_colors = []  # Reset temp_colors to a new list after appending

        # Append any remaining colors in temp_colors if it is not empty
        if temp_colors:
            colors_list.append(temp_colors)

        return colors_list

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = ProductModel.objects.all()
        context['categories'] = ProductCategoryModel.objects.all()
        context['manufactures'] = ProductManufacture.objects.all()
        context['tags'] = ProductTagModel.objects.all()
        context['colors'] = ProductColorModel.objects.all()
        return context


def add_or_remove(request, pk):
    cart = request.session.get('cart', [])
    if pk in cart:
        cart.remove(pk)

    else:
        cart.append(pk)

    request.session['cart'] = cart
    return redirect(request.GET.get('next', 'products:list'))


def add_or_remove_likes(request, pk):
    likes = request.session.get('likes', [])
    if pk in likes:
        likes.remove(pk)

    else:
        likes.append(pk)

    request.session['likes'] = likes
    return redirect(request.GET.get('nextt', 'products:list'))