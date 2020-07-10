from django import template

register=template.Library()


@register.filter(name='quantity')
def quantity(product, cart):
    keys=cart.keys()
    for i in keys:
        if int(i)==product.id:
            return cart.get(i)
    return 0    

@register.filter(name='total')
def total(product, cart):
    t=product.price*quantity(product, cart)
    return t

@register.filter(name='sum')
def sum(products, cart):                                   #getting entire products in cart
    s=0
    for i in products:
        s=s+total(i, cart)

    return s    