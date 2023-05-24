from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

from listings.views import listing_list, listing_retrieve, listing_create, listing_update, listing_delete, CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('', listing_list, name='index'),
    path('add-listing/', listing_create, name='listing_create'),
    path('listings/<pk>/', listing_retrieve, name='listing_retrieve'),
    path('listings/<pk>/edit/', listing_update, name='listing_update'),
    path('listings/<pk>/delete/', listing_delete, name='listing_delete'),
]
