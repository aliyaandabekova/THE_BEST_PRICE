from django.db import models
from userprofile.models import *

class Shop(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    rate = models.FloatField(default=0)
    amount_rate = models.FloatField(default=0)
    count_rate = models.PositiveIntegerField(default=0)
    avg_rate = models.FloatField(default=0)
    def __str__(self):
        return self.name


class Comment(models.Model):
    text = models.CharField(max_length=100)
    shop = models.ForeignKey(Shop,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)