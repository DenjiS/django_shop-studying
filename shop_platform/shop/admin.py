from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import Category, Product, Image


class ImagesInline(GenericStackedInline):
    model = Image


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [ImagesInline, ]


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [ImagesInline, ]
