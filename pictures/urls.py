from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # ex: /pictures/
    url('^$', views.home, name='home'),
    # ex: /pictures/test/
    url('<str:image_name>/', views.detail, name='detail'),
]
