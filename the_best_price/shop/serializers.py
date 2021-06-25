from rest_framework import serializers

class ScoreForShopSerializer(serializers.Serializer):
    score = serializers.FloatField()
