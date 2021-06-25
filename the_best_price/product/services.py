from django.shortcuts import render
import requests
from math import inf


def get_product(shops,product):
    # urls = {'eldorado':'http://192.168.2.133:8000/api/v1/eldorado/',
    #         'magnit':'http://192.168.2.133:8000/api/v1/magnit/',
    #         'gucci':'http://192.168.2.133:8000/api/v1/gucci/'}
    min_price = inf
    product_with_min_price = 0
    print(shops)
    for shop in shops:

        url = shop.url
        response = requests.get(url).json()
        for p in response:
            price = p['price']
            name = p['name']
            if product in name and price < min_price:
                min_price = price
                product_with_min_price = p
                product_with_min_price['shop'] = shop.name
    return product_with_min_price


def check_product_detail(shops,result):
    for shop in shops:
        url = shop.url
        response = requests.get(url).json()
        for p in response:
            if result.name in p['name'] and p['price'] < result.price:
                result.price = p['price']
                result.shop = shop.name
                result.save()
    return result









