from django import template

register = template.Library()

@register.filter
def price_toman_tag(price):
    return str(price) + ' تومان'