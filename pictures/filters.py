from .models import Image
import django_filters


class ImageFilter(django_filters.FilterSet):
    class Meta:
        model = Image
        fields = ['categories', 'location']
