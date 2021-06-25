from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from shop.models import *
from .services import *

class ShopView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            shop = Shop.objects.get(name=kwargs['shop_name'])
        except Shop.DoesNotExist:
            return Response('Такого магазина нет!')
        serializer = ScoreForShopSerializer(dat=request.data)
        if serializer.is_valid():
            if isinstance(request.user,AnonymousUser):
                return Response('Авторизуйтесь или зарегистрируйтесь!')
            profile = request.user.profile
            try:
                orders = profile.order_set.all()
                if check_order(orders,shop):
                    score = serializer.data.get('score')





