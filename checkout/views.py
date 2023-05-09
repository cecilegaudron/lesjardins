from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is currently empty")
        return redirect(revser('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51N5mSwLEDI49xDhmNP7srzG4meNISxldu7VRzNz0nofxxiQPf9ytK2sIZk5OgOyvRSfTdcMoczj2RlxdGvbUFcyD00pEtZsn3c',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)