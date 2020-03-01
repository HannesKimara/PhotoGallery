from django.test import TestCase
from .models import Category, Location, Image

class CategoryTestClass(TestCase):
    def setUp(self):
        self.new_category = Category(category = 'test_category')

    def test_isinstance(self):
        self.assertTrue(isinstance(self.new_category, Category))

    def test_save_category(self):
        self.new_category.save_model()
        self.all_categories = Category.objects.all()

        self.assertTrue(len(self.all_categories)>0)
    
    def test_delete_category(self):
        self.new_category.save()
        self.all_cat_precount = len(Category.objects.all())
        self.new_category.delete_model()
        self.all_cat_postcount = len(Category.objects.all())

        self.assertEqual(self.all_cat_postcount, 0)
        self.assertTrue(self.all_cat_postcount < self.all_cat_precount)

    def test_update_category(self):
        self.new_category.save()
        self.new_category.update_model(category = 'new_test_category')

        self.assertEqual(self.new_category.category, 'new_test_category')

    def tearDown(self):
        Category.objects.all().delete()


class LocationTestClass(TestCase):
    def setUp(self):
        self.new_location = Location(location = 'test_place')

    def test_isinstance(self):
        self.assertTrue(isinstance(self.new_location, Location))

    def test_save_location(self):
        self.new_location.save_model()
        self.all_locations_count = len(Location.objects.all())

        self.assertTrue(self.all_locations_count > 0)

    def test_delete_location(self):
        self.new_location.save()
        self.new_location.delete_model()
        self.all_locations_count = len(Location.objects.all())

        self.assertEqual(self.all_locations_count, 0)

    def test_update_location(self):
        self.new_location.save()
        self.new_location.update_model(location = 'new_test_location')

        self.assertEqual(self.new_location.location, 'new_test_location')

    def tearDown(self):
        Location.objects.all().delete()


class ImageTestClass(TestCase):
    def setUp(self):
        self.image_category = Category(category = 'test_category')
        self.image_category.save()
        self.image_location = Location(location = 'test_place')
        self.image_location.save()
        self.image = Image(image = "test_photo.png", image_name = "test_image_name", image_description = "A verbose Description", category = self.image_category, location = self.image_location)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.image, Image))

    def test_save_image(self):
        self.image.save_image()
        self.all_images_count = len(Image.objects.all())

        self.assertTrue(self.all_images_count > 0)

    def test_delete_image(self):
        self.image.save()
        self.image.delete_image()
        self.all_images_count = len(Image.objects.all())

        self.assertEqual(self.all_images_count,0)

    def test_update_image(self):
        self.image.save()
        self.image.update_image(image_name = 'new_test_image_name')

        self.assertEqual(self.image.image_name, 'new_test_image_name')

    def test_get_image_by_id(self):
        self.image.save()
        self.search_image = Image.get_image_by_id(self.image.id)

        self.assertEqual(self.search_image.image, self.image.image)

    def test_search_image(self):
        self.image.save()
        self.search_images = Image.search_image('test_category')

        self.assertTrue(all(isinstance(i, Image) for i in self.search_images))
        self.assertTrue(len(self.search_images) > 0)

    def test_filter_by_location(self):
        self.image.save()
        self.search_images_loc = Image.filter_by_location('test_place')
        
        self.assertTrue(all(isinstance(i, Image) for i in self.search_images_loc))
        self.assertTrue(len(self.search_images_loc) > 0)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()