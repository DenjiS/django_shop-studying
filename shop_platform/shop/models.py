from django.db import models


class Image(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/',
                              verbose_name='Image',
                              db_index=True)


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    main_image = models.ForeignKey('CategoryImage',
                                   on_delete=models.CASCADE,
                                   related_name='main_image',
                                   null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Categories'


class CategoryImage(Image):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    main_image = models.ForeignKey('ProductImage',
                                   on_delete=models.CASCADE,
                                   related_name='main_image',
                                   null=True, blank=True)


class ProductImage(Image):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
