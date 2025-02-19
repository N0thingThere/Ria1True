from django import template
register = template.Library()
@register.filter(name='get_quantity')
def get_cart_quantity(cart, movie_i):
    return cart[str(movie_i)]