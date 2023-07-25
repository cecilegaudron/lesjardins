from django.shortcuts import render, reverse, get_object_or_404, HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Wishlist, Product
from profiles.models import UserProfile


@login_required
def favourite_list(request):
    """
    Basic view to return the wishlist page
    """
    profile = get_object_or_404(UserProfile, user=request.user)

    favourites = profile.favourites.all()

    template = 'wishlist/wishlist.html'
    context = {
        'favourites': favourites,
        'on_profile_page': True
    }

    return render(request, template, context)


@login_required
def add_to_wishlist(request, item_id):
    """
    Basic view to add a product to the wishlist
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    item = get_object_or_404(Product, pk=item_id)

    favourites, created = profile.favourites.get_or_create(
        favourite=item,
        favourite_id=item.id,
    )
    messages.success(request, 'The product was added to your wishlist')
    return HttpResponseRedirect(reverse('product_detail', args=[str(item_id)]))


@login_required
def remove_to_wishlist(request, item_id):
    """
    Basic view to remove a product from the wishlist
    """
    profile = get_object_or_404(UserProfile, user=request.user)
    item = get_object_or_404(Product, pk=item_id)

    profile.favourites.filter(
        favourite=Product.objects.get(pk=item_id)
        ).delete()
    messages.success(request, 'The product was removed from your wishlist')
    return HttpResponseRedirect(reverse('product_detail', args=[str(item_id)]))
