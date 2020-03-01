from django.shortcuts import render, redirect
from .models import Image

def index(request):
    all_images = Image.objects.all()
    return render(request, 'index.html', {'images': all_images})

def search_results(request):
    if 'q' in request.GET and request.GET["q"]:
        query_item = request.GET.get("q")
        related_images = Image.search_image(query_item)
    else:
        return render(request, 'search.html', {'images': []})

    return render(request, 'search.html', {'images': related_images})