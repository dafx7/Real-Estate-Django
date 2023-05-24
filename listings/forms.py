from django.forms import ModelForm
from .models import Listing
from django import forms
from django.forms.widgets import ClearableFileInput


class ListingForm(ModelForm):

    class Meta:
        model = Listing
        fields = [
            'title',
            'price',
            'num_bedrooms',
            'num_bathrooms',
            'square_footage',
            'address',
        ]
