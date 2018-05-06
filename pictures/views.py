from django.http import HttpResponse
import datetime as dt
from .models import Image, Category, Location
# Create your views here.


def home(request):
    date = dt.date.today()
    latest_photos_list = Image.objects[:5]
    return HttpResponse(html)


def detail(request, image):
    response = "You're Looking at the image %s."
    return HttpResponse(response % image)
