from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    product = serializers.CharField()

class SavedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

