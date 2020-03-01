from django.db import models

class ModelMethods:
    def save_model(self):
        self.save()

    def delete_model(self):
        self.delete()

    def update_model(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
    
class Category(models.Model, ModelMethods):
    category = models.CharField(max_length = 64)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"

class Location(models.Model, ModelMethods):
    location = models.CharField(max_length = 64)

    def __str__(self):
        return self.location
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'gallery_images/')
    image_name = models.CharField(max_length= 60)
    image_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    def update_image(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    @classmethod
    def get_image_by_id(cls, image_id):
        _image = cls.objects.filter(pk = image_id)
        return _image

    @classmethod
    def search_image(cls, search_category):
        _images = cls.objects.filter(category__category=search_category)
        return _images
    
    @classmethod
    def filter_by_location(cls, search_location):
        _images = cls.objects.filter(location__location=search_location)
        return _images

    