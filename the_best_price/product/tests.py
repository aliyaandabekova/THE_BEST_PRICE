from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from shop.models import *
from userprofile.models import *

class ProductTest(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('product')
        self.shop = Shop.objects.create(name='eldorado',url='http://192.168.2.133:8000/api/v1/eldorado/')
        self.user = User.objects.create_user(username='aliya',password='123456')
        self.profile = Profile.objects.create(user=self.user,full_name='aliyaaaaa')
    def test_product(self):
        self.client.login(username='aliya',password='123456')
        data = {
            "product":"dress"
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code, 200)