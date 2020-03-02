from django.shortcuts import render, redirect
from .models import Image

def index(request):
    """
    index view function renders template for '/' view

    Args:
        request
    """
    all_images = Image.objects.all()
    return render(request, 'index.html', {'images': all_images})

def search_results(request):
    """
    search_results view function renders template for 'search/' view

    Args:
        request
    """
    if 'q' in request.GET and request.GET["q"]:
        query_item = request.GET.get("q")
        related_images = Image.search_image(query_item)
    else:
        return render(request, 'search.html', {'images': []})

    return render(request, 'search.html', {'images': related_images})

def filter_location(request, loc):
    """
    filter_location view function renders template for '/location' view

    Args:
        request
        loc (str): search parameter
    """
    loc_images = Image.filter_by_location(loc)

    return render(request, 'location.html', {'images': loc_images})