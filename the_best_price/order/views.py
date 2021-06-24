from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from userprofile.models import Profile
from .serializers import *





class MyOrderView(APIView):
    def get(self,request):
        profile = Profile.objects.get(user=request.user)
        orders = profile.order_set.all()
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data, status=200)