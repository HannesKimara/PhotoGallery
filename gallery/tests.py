from django.test import TestCase
from .models import Category, Location, Image

class CategoryTestClass(TestCase):
    def setUp(self):
        self.new_category = Category(category = 'test_category')

    def test_isinstance(self):
        self.assertTrue(isinstance(self.new_category, Category))

class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location = Location(location = 'test_place')

    def test_isinstance(self):
        self.assertTrue(isinstance(self.new_location, Location))

class ImageTestClass(TestCase):
    def setUp(self):
        self.image_category = Category(category = 'test_category')
        self.image_location = Location(location = 'test_place')
        self.image = Image(image = "test_photo.png", image_name = "test_image_name", image_description = "A verbose Description", category = self.image_category, location = self.image_location)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.image, Image))
