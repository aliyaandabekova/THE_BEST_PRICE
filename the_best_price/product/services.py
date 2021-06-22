from django.shortcuts import render
import requests
from math import inf


def get_product(product):
    urls = ['http://192.168.2.133:8000/api/v1/eldorado/','http://192.168.2.133:8000/api/v1/magnit/','http://192.168.2.133:8000/api/v1/gucci/']
    min_price = inf
    product_with_min_price = 0
    for url in urls:
        response = requests.get(url).json()
        for p in response:
            price = p['price']
            name = p['name']
            if product in name and price < min_price:
                min_price = price
                product_with_min_price = p
    return product_with_min_price





