from django.http import HttpResponse
from .models import Order, OrderLineItem
from products.models import Product
from profiles.models import UserProfile
import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        bag = intent.metadata.bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
            )

        billing_details = stripe_charge.billing_details  # updated
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)  # updated

        # Update profile information if save_info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_country = shipping_details.address.country
                profile.default_postcode = shipping_details.address.postal_code
                profile.default_city = shipping_details.address.city
                profile.default_street_address1 = shipping_details.address.street_address1
                profile.default_street_address2 = shipping_details.address.street_address2
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.full_name,
                    email__iexact=billing_details.email,
                    country__iexact=shipping_details.address.country,
                    postcode__iexact=shipping_details.address.postal_code,
                    city__iexact=shipping_details.address.city,
                    street_address1__iexact=shipping_details.address.street_address1,
                    street_address2__iexact=shipping_details.address.street_address2,
                    grand_total=grand_total,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} \
                    | SUCCESS : Verified order alread in database',
                status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    country=shipping_details.address.country,
                    postcode=shipping_details.address.postal_code,
                    city=shipping_details.address.city,
                    street_address1=shipping_details.address.street_address1,
                    street_address2=shipping_details.address.street_address2,
                    original_bag=bag,
                    stripe_pid=pid,
                )
                for item_id, item_data in json.loads(bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} \
                    | ERROR : {e}', status=500)
        return HttpResponse(
            content=f'Webhook received: {event["type"]} \
                    | SUCCESS : Created order in webhook', status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
