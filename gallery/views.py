from django.shortcuts import render
from .models import Image

def index(request):
    all_images = Image.objects.all()
    return render(request, 'index.html', {'images': all_images})