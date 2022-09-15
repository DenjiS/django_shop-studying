from django.db import models
from django.core.files.storage import FileSystemStorage


def get_path(instance, filename):
    # file will be uploaded to /media/images/type/id/<filename>
    return f'images/{instance.relation}/{instance.id}/{filename}'


class Image(models.Model):
    image = models.ImageField(upload_to=get_path,
                              verbose_name='Image',
                              db_index=True)

    @property
    def relation(self):
        return self.__class__.__name__


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()

    # TODO: main image

    def __str__(self):
        return self.name


class CategoryImage(Image):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Good(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    category = models.ManyToManyField(Category)

    # TODO: main image

    def __str__(self):
        return self.name


class GoodImage(Image):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
