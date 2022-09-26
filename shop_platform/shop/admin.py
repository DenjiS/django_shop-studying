from django.contrib import admin
from .models import Category, Product, Image, ImageAlbum


class ImagesInline(admin.StackedInline):
    model = Image


@admin.register(ImageAlbum)
class ImageAlbumAdmin(admin.ModelAdmin):
    inlines = [ImagesInline,]


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
