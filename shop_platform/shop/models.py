from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    default = models.BooleanField(default=False)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    def save(self, **kwargs):
        if self.default:
            Image.objects.filter(content_type=self.content_type, object_id=self.object_id).update(default=False)
        super().save(**kwargs)


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    images = GenericRelation(Image)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField(Category)
    images = GenericRelation(Image)

    def __str__(self):
        return self.name
