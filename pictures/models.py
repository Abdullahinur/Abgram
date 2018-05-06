from django.db import models


# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    def save_locations(self):
        self.save()

    def delete_locations(self):
        self.delete()


class Category(models.Model):
    name = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name

    def save_categories(self):
        self.save()

    def delete_categories(self):
        self.delete()


class Image(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    image_name = models.CharField(max_length=30, null=True)
    image_description = models.CharField(max_length=3000, null=True)
    location = models.ForeignKey(Location, null=True)
    categories = models.ForeignKey(Category, null=True)

    def __str__(self):
        return self.image_name

    def save_images(self):
        self.save()

    def delete_images(self):
        self.delete()
