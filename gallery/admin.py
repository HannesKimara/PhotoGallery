from django.contrib import admin
from .models import Category, Location, Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ('image_name','image_description', 'location', 'category', 'pub_date')
    date_hierarchy = 'pub_date'
    ordering = ['-pub_date']

admin.site.register(Category)
admin.site.register(Location)
admin.site.register(Image, ImageAdmin)
