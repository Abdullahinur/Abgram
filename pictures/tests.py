from django.test import TestCase
from .models import Image, Location, Category
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

    def test_update_image(self):
        self.image.save_images()
        self.image.update_image('abdullahinur', 'new_description', 'new_image_url')
        self.image.save_images()
        updated_name = self.image.image_name
        update_description = self.image.image_description
        updated_url = self.image.image
        self.assertTrue(updated_name == 'abdullahinir' and update_description ==
                        'new_description', updated_url == 'new_image_url')


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


class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.category = Category(name='test_category')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_categories(self):
        self.category.save_categories()
        categories = Category.objects.all()
        self.assertTrue(len(categories) > 0)

    def test_delete_categories(self):
        self.category.save_categories()
        self.category.delete_categories()
        categories = Category.objects.all()
        self.assertTrue(len(categories) == 0)
