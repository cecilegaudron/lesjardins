from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower
from .models import Product, Category
from .forms import ProductForm


def all_products(request):
    """
    Basic view for the all products page including sorting and search queries
    A context is required to send some things back to the template
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

            if sortkey == 'category':
                """
                Force the categories to be displayed by name instead of the ID
                """
                sortkey = 'category__name'

            if 'direction' in request.GET:
                """
                Check the direction if it is descending, reverse the order \
                with the minus in front of the sortkey
                """
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'

            products = products.order_by(sortkey)

        if 'category' in request.GET:
            """
            If statement for category search
            Check if the category exists
            Filter all categories to the ones choosen by its name
            """
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            """
            If statement for the search form
            Check if the text input is equal to a variable called query
            If the query is blank any results are returned but a message \
                and redirect to the products page
            """
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search critera")
                return redirect(reverse('products'))

            """
            If the name or the description containes the query
            The pipe generates the or statement
            the i makes the queries case insensitive
            """
            queries = Q(name__icontains=query) \
                | Q(description__icontains=query)
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


@login_required
def add_product(request):
    """Add product to the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry you are not an admin, you can not do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'You added a product with success')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Adding product failes. \
                Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """Edit a product in the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry you are not an admin, you can not do that.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Updating product failed. \
                Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }
    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """Delete a product from the store"""
    if not request.user.is_superuser:
        messages.error(request, 'Sorry you are not an admin, you can not do that.')
        return redirect(reverse('home'))
    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Products deleted!')
    return redirect(reverse('products'))
