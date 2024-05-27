from django.contrib import admin
from products.models import *


@admin.register(ProductColorModel)
class ProductColorModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at',)
    search_fields = ('name',)
    list_filter = ( 'created_at',)

@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at',)
    search_fields = ('name',)
    list_filter = ( 'created_at',)

@admin.register(ProductTagModel)
class ProductTagModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at',)
    search_fields = ('name',)
    list_filter = ( 'created_at',)

@admin.register(ProductSizeModel)
class ProductSizeModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at',)
    search_fields = ('name',)
    list_filter = ( 'created_at',)

@admin.register(ProductManufactureModel)
class ProductManufactureModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at',)
    search_fields = ('name',)
    list_filter = ( 'created_at',)

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('name','created_at',)
    search_fields = ('name',)
    list_filter = ( 'created_at',)