def check_order(orders,shop):
    for order in orders:


        if order.product.shop == shop.name:
            return True



def count_avg_score(shop, score):
    shop.rate = score
    shop.amount_rate += shop.rate
    shop.count_rate += 1
    shop.avg_rate = shop.amount_rate / shop.count_rate
    shop.avg_rate = round(shop.avg_rate,2)
    shop.save()
