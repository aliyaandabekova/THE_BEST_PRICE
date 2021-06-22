from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
    shop = models.CharField(max_length=20,null=True,blank=True)
    def __str__(self):
        return self.name
