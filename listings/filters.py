import django_filters
from django_filters import RangeFilter
from .models import *


class ListingFilter(django_filters.FilterSet):
    num_bedrooms = RangeFilter(field_name='num_bedrooms')
    num_bathrooms = RangeFilter(field_name='num_bathrooms')
    square_footage = RangeFilter(field_name='square_footage')
    price = RangeFilter(field_name='price')

    class Meta:
        model = Listing
        fields = '__all__'
        exclude = ['title', 'price', 'num_bedrooms',
                   'num_bathrooms', 'square_footage']
