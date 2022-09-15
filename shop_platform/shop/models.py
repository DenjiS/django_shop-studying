from django.db import models


def get_path(instance, filename):
    # file will be uploaded to /media/images/type/id/<filename>
    return f'images/{instance.relation}/{filename}'


class Image(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to=get_path,
                              verbose_name='Image',
                              db_index=True)

    @property
    def relation(self):
        return self.__class__.__name__

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    main_image = models.ForeignKey('CategoryImage',
                                   on_delete=models.CASCADE,
                                   related_name='main_image',
                                   null=True, blank=True)

    def __str__(self):
        return self.name


class CategoryImage(Image):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Good(models.Model):
    name = models.CharField(max_length=20)
    description = models.TextField()
    category = models.ManyToManyField(Category)
    main_image = models.ForeignKey('GoodImage',
                                   on_delete=models.CASCADE,
                                   related_name='main_image',
                                   null=True, blank=True)

    def __str__(self):
        return self.name


class GoodImage(Image):
    good = models.ForeignKey(Good, on_delete=models.CASCADE)
