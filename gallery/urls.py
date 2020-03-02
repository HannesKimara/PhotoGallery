from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('search', views.search_results, name = 'search_results'),
    path('location/<str:loc>', views.filter_location, name = 'filter_location')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)