from django import template

register = template.Library()

""" django documentation about creating custom template tags and filters """
@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity