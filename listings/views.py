from typing import Any, Dict
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView, CreateView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required


from .models import Listing, ListingImage
from .forms import ListingForm

# Create your views here.

# Login View


class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('index')


# Register View
class RegisterPage(FormView):
    template_name = 'register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('index')
        return super(RegisterPage, self).get(*args, **kwargs)


# CRUDL - create, retrieve, update, delete, list

@login_required
def listing_list(request):
    listings = Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, "listings.html", context)


@login_required
def listing_retrieve(request, pk):
    listing = Listing.objects.get(id=pk)
    images = listing.images.all
    context = {
        'listing': listing,
        'images': images,
    }
    return render(request, 'listing.html', context)


@login_required
def listing_create(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST)
        images = request.FILES.getlist('images')
        if form.is_valid():
            listing = form.save()
            for i in images:
                ListingImage(listing=listing, image=i).save()
            return redirect('/')

    context = {
        'form': form,
    }
    return render(request, 'listing_create.html', context)


@login_required
def listing_update(request, pk):
    listing = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)

    if request.method == "POST":
        form = ListingForm(request.POST, instance=listing)
        images = request.FILES.getlist('images')
        if form.is_valid():
            listing = form.save()
            ListingImage.objects.all().filter(listing=listing).delete()
            for i in images:
                ListingImage(listing=listing, image=i).save()
            return redirect('/')

    context = {
        'form': form,
        'id': listing.id,
    }
    return render(request, 'listing_update.html', context)


@login_required
def listing_delete(request, pk):
    listing = Listing.objects.get(id=pk)
    if request.method == "POST":
        listing.delete()
        return redirect('/')

    context = {
        'listing': listing,
        'id': listing.id,
    }
    return render(request, 'listing_delete.html', context)
