from django.db import models

class Wall(models.Model):
    image = models.ImageField(upload_to = 'images/')
    category = models.ManyToManyField('Category')
    device = models.ForeignKey('Device', on_delete = models.PROTECT)

class Category(models.Model):
    name = models.CharField(max_length = 150)

    def __str__(self):
        return self.name

class Device(models.Model):
    title = models.CharField(max_length = 150)

    def __str__(self):
        return self.title
