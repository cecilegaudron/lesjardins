from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Wishlist, Product


# https://data-flair.training/blogs/python-django-wishlist-app
def favourite_list(request):
    """
    Basic view to return the wishlist page
    """
    user = request.user
    favourite = Wishlist.objects.all()

    context = {
        'favourites': favourite
    }

    return render(request, 'wishlist/wishlist.html', context)
