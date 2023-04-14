from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product


def all_products(request):
    """
    Basic view for the all products page including sorting and search queries
    A context is required since we need to send some thinds back to the template
    Import the product model and all products from the database
    The products can be available in the template
    """

    products = Product.objects.all()
    query = None

    if request.GET :
        """
        If statement for the search form
        Check if the text input is equal to a variable called query
        If the query is blank any results are returned but a message and redirect to the products page
        """
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search critera")
                return redirect(reverse('products'))

            """
            If the name or the description containes the query
            The pipe generates the or statement
            the i makes the queries case insensitive
            """
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    context = {
        'products': products,
        'search_term': query,
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
