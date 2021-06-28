from rest_framework import serializers
from .models import *

class ScoreForShopSerializer(serializers.Serializer):
    score = serializers.FloatField()


class CommentSerializer(serializers.Serializer):
    text = serializers.CharField()


class CommentGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ShopSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True)
    class Meta:
        model = Shop
        fields = ['name','url','avg_rate','comment_set']
