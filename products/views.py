from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Product, Category


def all_products(request):
    """
    Basic view for the all products page including sorting and search queries
    A context is required since we need to send some thinds back to the template
    Import the product model and all products from the database
    The products can be available in the template
    """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        """
        If statement for sort display, price or category
        If a direction is added on main_nav file, apply it, asc or desc
        """
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                """
                Rename sortkey to lower_name to not lost the original field
                """
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            """
            Check the direction if it is descending, reverse the order with the minus in front of the sortkey
            """
            if 'direction' in request.GET :
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            """
            Use the order by model method
            """
            products = products.order_by(sortkey)

        """
        If statement for category search
        Check if the category exists
        Filter all categories to the ones choosen by its name
        """
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

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

    """
    Return the current sorting methodology to the template
    """
    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
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
