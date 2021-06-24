from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=50)
    email = models.EmailField(null=True,blank=True)
    address = models.CharField(max_length=30,null=True,blank=True)
    def __str__(self):
        return self.full_name

