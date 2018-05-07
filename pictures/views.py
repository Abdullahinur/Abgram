from django.http import HttpResponse, Http404
import datetime as dt
from django.shortcuts import render
from .models import Image
from .filters import ImageFilter
# Create your views here.


def home(request):
    date = dt.date.today()
    slogan = 'Just keep uploading...'
    pictures = Image.get_images()
    return render(request, 'index.html', {"date": date, "slogan": slogan, "pictures": pictures})


def image(request, image_name):
    try:
        image = Image.objects.get(name=image_name)
    except DoesNotExist:
        raise Http404()
    return render(request, 'images/image.html', {"image": image})


def search(request):
    image_list = Image.objects.all()
    image_filter = ImageFilter(request.GET, queryset=image_list)
    return render(request, 'search.html', {"filter": image_filter})
