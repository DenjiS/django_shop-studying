from django.db import models


class ImageAlbum(models.Model):
    def default(self):
        return self.images.filter(default=True).first()


class Image(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)
    album = models.ForeignKey(ImageAlbum, related_name='images', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    album = models.OneToOneField(ImageAlbum, related_name='cat_model', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    album = models.OneToOneField(ImageAlbum, related_name='prod_model', on_delete=models.CASCADE)

    def __str__(self):
        return self.name
