from django.test import TestCase
from .models import Image
# Create your tests here.


class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.image = Image(image='imageurl', image_name='test_image',
                           image_description='image test description')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_images(self):
        self.image.save_images()
        images = Image.objects.all()
        self.assertTrue(len(images) > 0)

    def test_delete_images(self):
        self.image.save_images()
        self.image.delete_images()
        images = Image.objects.all()
        self.assertTrue(len(images) == 0)


class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.location = Location(name='test_location')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_locations(self):
        self.location.save_locations()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_locations(self):
        self.location.save_locations()
        self.location.delete_locations()
        locations = Location.objects.all()
        self.assertTrue(len(locations) == 0)
