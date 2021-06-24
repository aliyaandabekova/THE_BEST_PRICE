from django.db import models
from userprofile.models import Profile
from product.models import Product

class Order(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL,null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null=True)

