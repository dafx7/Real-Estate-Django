import django_filters
from django_filters import RangeFilter
from .models import *


class ListingFilter(django_filters.FilterSet):
    price = RangeFilter(field_name='price')

    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['title', 'price']
