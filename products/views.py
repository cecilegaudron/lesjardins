from django.shortcuts import render
from .models import Product


def all_products(request):
    """
    Basic view for the all products page including sorting and search queries
    A context is required since we need to send some thinds back to the template
    Import the product model and all products from the database
    The products can be available in the template
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }

    return render(request, 'products/products.html', context)
