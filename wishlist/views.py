from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib import messages
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


def add_to_wishlist(request, item_id):
    """
    Basic View for adding a product to the wishlist
    """
    item = get_object_or_404(Product, pk=item_id)

    favourite, created = Wishlist.objects.get_or_create(
        favourite=item,
        favourite_id=item.id,
        user=request.user,
    )
    messages.info(request, 'The item was added to your wishlist')
    return HttpResponseRedirect(reverse('product_detail', args=[str(item_id)]))

