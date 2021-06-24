from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from product.models import Score

from .models import *

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['full_name','email','address']


class RegisterSerializer(serializers.ModelSerializer):
    check_password = serializers.CharField(min_length=6)
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['username','password','check_password','profile']

    def create(self,validated_data):
        password = validated_data.get('password')
        check_password = validated_data.pop('check_password')
        profile_data = validated_data.pop('profile')
        if password == check_password:
            user = User.objects.create(**validated_data)
            Profile.objects.create(user=user,**profile_data)
            return user
        raise ValidationError("Passwords don't match. Try again!")


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=5)
    password = serializers.CharField(min_length=5)


class ScoreSerializer(serializers.Serializer):
    score = serializers.FloatField(min_value=1.0,max_value=5.0)


class GetScoreSerializer(serializers.ModelSerializer):
    # product = StringRelated
    class Meta:
        model = Score
        fields = '__all__'
