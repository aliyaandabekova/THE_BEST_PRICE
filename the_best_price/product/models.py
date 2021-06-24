from django.db import models
from userprofile.models import Profile

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    shop = models.CharField(max_length=20,null=True,blank=True)
    score_from_api = models.FloatField()
    score_of_our_users = models.FloatField(default=0)  #average
    def __str__(self):
        return self.name


class Score(models.Model):
    profile = models.ForeignKey(Profile,on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    score = models.FloatField()