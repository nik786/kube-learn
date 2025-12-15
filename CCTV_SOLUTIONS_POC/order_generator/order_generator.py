import copy
import random

from uuid import uuid4

from collections import namedtuple

Product = namedtuple('Product', ['code', 'name', 'price'])

products = [
    Product('cc01', 'dome camera', '$20'),
    Product('cc02', 'bullet camera', '$35'),
    Product('cc03', 'solar camera', '$45'),
    Product('cc04', 'ip camera', '$55')
]

seller_ids = ['abc', 'xyz', 'jkq', 'wrp']
customer_ids = [
    "cc01", "cc02", "cc03", "cc04", "cc05", "cc06", "cc07", "cc08", "cc09", "cc10",
    "cc11", "cc12", "cc13", "cc14", "cc15", "cc16", "cc17", "cc18", "cc19", "cc20",
]


def make_order():
    order_id = str(uuid4())
    seller_id = random.choice(seller_ids)
    customer_id = random.choice(customer_ids)
    order_items = []

    available_products = copy.copy(products)
    n_products = random.randint(1, len(products))
    for _ in range(n_products):
        product = random.choice(available_products)
        available_products.remove(product)
        qty = random.randint(1, 10)

        order_items.append({
            'product_name': product.name,
            'product_code': product.code,
            'product_quantity': qty,
            'product_price': product.price
        })

    order = {
        'customer_id': customer_id,
        'seller_id': seller_id,
        'order_id': order_id,
        'order_items': order_items
    }
    return order
