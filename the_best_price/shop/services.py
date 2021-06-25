def check_order(orders,shop):
    for order in orders:
        if order.product.shop == shop.name:
            return True