from django.http import HttpResponse
import datetime as dt
from django.shortcuts import render
from .models import Category, Image, Location
# Create your views here.


def home(request):
    date = dt.date.today()
    slogan = 'Just keep uploading...'
    pictures = Image.get_images()
    return render(request, 'index.html', {"date": date, "slogan": slogan, "pictures": pictures})


def detail(request, image):
    response = "You're Looking at the image %s."
    return HttpResponse(response % image)
