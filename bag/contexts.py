""" Decimal function is preferred when working with money because it is accurate """
from decimal import Decimal
""" Import the settings about the free delivery """
from django.conf import settings

def bag_contents(request):
    """
    Function returns a dictionary called context processor
    The dictionary is avaialble to all templates
    """
    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    
    """Checker if the amount to pay is less than the total threshold
    If yes, the delivery is calculated as the total multiplied by the standard delivery percentage so 10%
    """
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE/100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total

    else:
        delivery = 0
        free_delivery_delta = 0
    
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }

    return context