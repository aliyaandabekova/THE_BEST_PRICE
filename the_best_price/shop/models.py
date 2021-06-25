from django.db import models

class Shop(models.Model):
    name = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
    rate = models.FloatField(default=0)
    # def __str__(self):
    #     return self.name
