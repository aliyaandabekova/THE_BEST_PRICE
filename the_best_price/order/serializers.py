from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from .models import Order

class MyOrderSerializer(serializers.ModelSerializer):
    profile = StringRelatedField()
    product = StringRelatedField()
    class Meta:
        model = Order
        fields = '__all__'
