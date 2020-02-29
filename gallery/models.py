from django.db import models

# Create your models here.

class Category(models.Model):
    category = models.CharField(max_length = 64)

class Location(models.Model):
    location = models.CharField(max_length = 64)
    
class Image(models.Model):
    image = models.ImageField(upload_to = 'images/')
    image_name = models.CharField(max_length= 60)
    image_description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add = True)
    location = models.ForeignKey(Location, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)