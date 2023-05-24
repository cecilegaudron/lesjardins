from django.shortcuts import render, reverse, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Wishlist
from products.models import Product


@login_required
def wishlist(request):
    """
    See the wishlist
    """
    products = Product.objects.filter(users_wishlist=request.user)
    return render(request, 'wishlist/wislist.html', {'wishlist': products})


@login_required
def add_wishlist(request, id):
    """
    Add a product to the wishlist
    """
    if request.user.is_authenticated:
        user = request.user

        product = get_object_or_404(Product, id=id)
        if product.users_wishlist.filter(id=request.user.id).exists():
            product.users_wishlist.remove(request.user)
        else:
            product.users_wishlist.add(request.user)
            messages.success(request, 'Product added to wishlist!')
        return HttpResponseRedirect(request.META["HTTP_REFERER"])

    else:
        messages.error(request, 'You need to be logged into your account to perform this action.')
