from django.contrib import admin
from .models import Category, Good, CategoryImage, GoodImage


class ImagesCategoryInline(admin.StackedInline):
    model = CategoryImage


class ImagesGoodInline(admin.StackedInline):
    model = GoodImage


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    radio_fields = {'main_image': admin.HORIZONTAL}
    inlines = [
        ImagesCategoryInline,
    ]


@admin.register(Good)
class GoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    radio_fields = {'main_image': admin.HORIZONTAL}
    inlines = [
        ImagesGoodInline,
    ]
