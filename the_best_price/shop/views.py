from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from shop.models import *
from .services import *
from order.models import *
from .models import *

class ShopScoreView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            shop = Shop.objects.get(name=kwargs['shop_name'])
        except Shop.DoesNotExist:
            return Response('Такого магазина нет!')
        serializer = ScoreForShopSerializer(data=request.data)
        if serializer.is_valid():
            if isinstance(request.user,AnonymousUser):
                return Response('Авторизуйтесь или зарегистрируйтесь!')
            profile = request.user.profile
            try:
                orders = profile.order_set.all()
                if check_order(orders,shop):
                    score = serializer.data.get('score')
                    count_avg_score(shop,score)
                    serializer1 = ShopSerializer(shop)
                    return Response(serializer1.data,status=201)
                else:
                    return Response('У вас нет заказов с этого магазина!')
            except Order.DoesNotExist:
                return Response('У вас нет заказов!')
        return Response(serializer.errors,status=400)

class ShopsView(APIView):
    def get(self,request):
        shops = Shop.objects.all()
        serializer = ShopSerializer(shops,many=True)
        return Response(serializer.data,status=200)

class CommentView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            shop = Shop.objects.get(name=kwargs['shop_name'])
        except Shop.DoesNotExist:
            return Response('Такого магазина нет!')
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            if isinstance(request.user,AnonymousUser):
                return Response('Авторизуйтесь или зарегистрируйтесь!')
            profile = request.user.profile
            try:
                orders = profile.order_set.all()
                if check_order(orders,shop):
                    comment_object = Comment.objects.create(profile=profile,shop=shop,text=request.data['text'])
                    serializer1 = CommentGetSerializer(comment_object)
                    return Response(serializer1.data,status=201)
                return Response('У вас нет заказов с этого магазина!')
            except Order.DoesNotExist:
                return Response('У вас нет заказов!')
        return Response(serializer.errors,status=400)


















