from django.db import models

class ModelMethods:
    """
    Define CRUD operation methods for db models
    """
    def save_model(self):
        """
        Save relational model data to database

        Args:
            self:self
        Returns:
            None (NoneType)
        """
        self.save()

    def delete_model(self):
        """
        Delete relational model data from database

        Args:
            self:self
        Returns:
            None (NoneType)
        """
        self.delete()

    def update_model(self, **kwargs):
        """
        Update relational model data in database

        Args:
            kwargs: model attributes to be updated
        Returns:
            None (NoneType)
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()
    
class Category(models.Model, ModelMethods):
    """
    Relationship Mapper for Category table

    Args:
        models.Model: Extends models.Model from django.db
        ModelMethods: Extends ModelMethods class containing CRUD database methods
    """
    category = models.CharField(max_length = 64)

    def __str__(self):
        return self.category

    class Meta:
        verbose_name_plural = "Categories"

class Location(models.Model, ModelMethods):
    """
    Relationship Mapper for Location table

    Args:
        models.Model: Extends models.Model from django.db
        ModelMethods: Extends ModelMethods class containing CRUD database methods
    """
    location = models.CharField(max_length = 64)

    def __str__(self):
        return self.location
    
class Image(models.Model):
    """
    Relationship Mapper for Image table

    Args:
        models.Model: Extends models.Model from django.db
    """
    image = models.ImageField(upload_to = 'gallery_images/')
    image_name = models.CharField(max_length= 60)
    image_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)

    def save_image(self):
        """
        Save image to database

        Args:
            self:self
        Returns:
            None (NoneType)
        """
        self.save()

    def delete_image(self):
        """
        Delete image from database

        Args:
            self:self
        Returns:
            None (NoneType)
        """
        self.delete()

    def update_image(self, **kwargs):
        """
        Update image data in database

        Args:
            self:self
            kwargs:attributes to be updated in database model. Accepted attributes are image, image_name (str), image_description (str), pub_date (datetime), location (Location), category (Category)
        Returns:
            None (NoneType)
        """
        for key, value in kwargs.items():
            setattr(self, key, value)
        self.save()

    @classmethod
    def get_image_by_id(cls, image_id):
        """
        Query Image from database by Image id/primary_key

        Args:
            image_id (int): id of image in database also primary_key
        Returns:
            instance of Image
        """
        _image = cls.objects.filter(pk = image_id).first()
        return _image

    @classmethod
    def search_image(cls, search_category):
        """
        Query Images from database by category

        Args:
            search_category (str): Category of Image

        Returns:
            QuerySet of matching images
        """
        _images = cls.objects.filter(category__category=search_category)
        return _images
    
    @classmethod
    def filter_by_location(cls, search_location):
        """
        Filter Images by location of image

        Args:
            search_location (str): Location of Image
        Returns:
            QuerySet of filtered images
        """
        _images = cls.objects.filter(location__location=search_location)
        return _images

    