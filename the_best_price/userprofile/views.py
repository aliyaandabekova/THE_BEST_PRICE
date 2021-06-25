from django.contrib.auth import authenticate, login
from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .models import *
from order.models import Order
from product.models import Product,Score
from .services import *



class RegisterView(APIView):
    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Successfully register!',status=201)
        return Response(serializer.errors,status=400)



class ProfileView(APIView):
    def get(self,request):
        try:
            profile = Profile.objects.get(user=request.user)
            serializer = ProfileSerializer()
        except Profile.DoesNotExist:
            return Response('404',status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self,request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response('Your profile is update!',status=200)
        return Response(serializer.errors,status=400)
    def delete(self,request):
        profile = Profile.objects.get(user=request.user)
        profile.delete()
        return Response('Your profile is deleted!',status=200)



class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.data.get('username')
            password = serializer.data.get('password')
            user = authenticate(username=username,password=password)
            login(request,user)
            return Response('Welcome to our site!')
        return Response(serializer.errors)


class ScoreView(APIView):
    def post(self,request,*args,**kwargs):
        try:
            product = Product.objects.get(id=kwargs['product_id'])
        except Product.DoesNotExist:
            return Response("Такого продукта нет!")
        serializer = ScoreSerializer(data=request.data)
        if serializer.is_valid():
            if isinstance(request.user,AnonymousUser):
                return Response('Авторизуйтесь или зарегистрируйтесь!')
            profile = request.user.profile
            try:
                order = Order.objects.get(product=product,profile=profile)
                score = serializer.data.get('score')
                score_object = Score.objects.create(profile=profile,product=product,score=score)
                scores_of_product = Score.objects.filter(product=product)
                product.score_of_our_users = calculate_avg_score(scores_of_product)
                product.save()
                serializer1 = GetScoreSerializer(score_object)
                return Response(serializer1.data,status=201)
            except Order.DoesNotExist:
                return Response('Данный товар не входит в список ваших заказов!',status=404)
        return Response(serializer.errors,status=400)




