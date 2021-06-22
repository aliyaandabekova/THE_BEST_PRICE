from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from .services import get_product
from .models import *



class ProductView(APIView):
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            product = serializer.data.get('product')
            result = get_product(product)
            Product.objects.create(name=result['name'],price=result['price'])
            serializer1 = GetProductSerializer
            return Response(result,status=200)




