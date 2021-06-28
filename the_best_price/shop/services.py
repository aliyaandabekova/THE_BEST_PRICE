def check_order(orders,shop):
    for order in orders:


        if order.product.shop == shop.name:
            return True



def count_avg_score(shop, score):
    shop.rate = score
    shop.amount_rate += shop.rate
    shop.count_rate += 1
    shop.avg_rate = shop.amount_rate / shop.count_rate
    shop.save()
