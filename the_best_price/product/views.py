from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .services import *
from .models import *
from order.models import Order
from shop.models import *



class ProductView(APIView):
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.data.get('product')
            shops = Shop.objects.all()
            try:
                result = Product.objects.get(name__contains=product)
                Order.objects.create(profile=request.user.profile, product=result)
                check_product_detail(shops,result)
                result = SavedProductSerializer(result).data
                return Response({"Из текущей базы:": result}, status=200)
            except Product.DoesNotExist:
                result = get_product(shops,product)
                print(result)
                prod = Product.objects.create(name=result['name'],price=result['price'],shop=result['shop'], score_from_api=result['score'])
                Order.objects.create(profile=request.user.profile, product=prod)
                return Response(result,status=200)




