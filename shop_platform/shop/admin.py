from django.contrib import admin
from .models import Category, Product, CategoryImage, ProductImage


class ImagesCategoryInline(admin.StackedInline):
    model = CategoryImage


class ImagesProductInline(admin.StackedInline):
    model = ProductImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    radio_fields = {'main_image': admin.HORIZONTAL}
    inlines = [
        ImagesCategoryInline,
    ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    radio_fields = {'main_image': admin.HORIZONTAL}
    inlines = [
        ImagesProductInline,
    ]
