from django.http import HttpResponse, Http404
import datetime as dt
from django.shortcuts import render
from .models import Category, Image, Location
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
