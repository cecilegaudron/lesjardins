from django.shortcuts import render, get_object_or_404
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


def product_detail(request, product_id):
    """
    Basic view for individual product details
    With the product_id as a parameter to return one product
    If no product to display the 404 error page appears
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)
