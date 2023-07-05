from django.shortcuts import render, reverse, get_object_or_404, HttpResponseRedirect, HttpResponse
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
        'favourites': favourite,
        'product': product,
        'is_favourite': is_favourite,
    }

    return render(request, 'wishlist/wishlist.html', context)


def favourite_product(request, item_id):
    """ A view to show individual product details """

    item = get_object_or_404(Product, pk=item_id)
    is_favourite = False

    if product.favourites.filter(id=request.user.id).exists():
        is_favourite = True

    context = {
        'product': product,
        'is_favourite': is_favourite,
    }

    return render(request, 'products/product_detail.html', context)


# https://stackoverflow.com/questions/56580696/how-to-implement-add-to-wishlist-for-a-product-in-django
def add_to_wishlist(request, item_id):
    """
    Basic view to add a product to the wishlist
    """
    item = get_object_or_404(Product, pk=item_id)

    favourite, created = Wishlist.objects.get_or_create(
        favourite=item,
        favourite_id=item.id,
        user=request.user,
    )
    messages.success(request, 'The product was added to your wishlist')
    return HttpResponseRedirect(reverse('product_detail', args=[str(item_id)]))


# https://stackoverflow.com/questions/63444550/how-to-delete-product-from-wishlist-in-django
def remove_to_wishlist(request, item_id):
    """
    Basic view to remove a product from the wishlist
    """
    Wishlist.objects.filter(
        user=request.user,
        favourite=Product.objects.get(pk=item_id)).delete()
    messages.success(request, 'The product was removed from your wishlist')
    return HttpResponseRedirect(reverse('product_detail', args=[str(item_id)]))
