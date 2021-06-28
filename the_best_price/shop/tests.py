from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from shop.models import *
from userprofile.models import *
from order.models import *
from product.models import *

class ScoreShopTest(APITestCase):
    def setUp(self) -> None:
        self.shop = Shop.objects.create(name='DG',url='http://192.168.2.133:8000/api/v1/magnit/')
        self.user = User.objects.create_user(username='aliya',password='123456')
        self.profile = Profile.objects.create(user=self.user,full_name='aliyaaaaaa')
        self.product = Product.objects.create(name='dress',price=500,score_from_api=4.0,shop=self.shop)
        self.order = Order.objects.create(profile=self.profile,product=self.product)
        self.url = reverse('shop_score',args=(self.shop.name,))
    def test_shop_score(self):
        self.client.login(username='aliya',password='123456')
        x = 5
        data = {
            "score":x
        }
        self.response = self.client.post(self.url,data).json()
        assert x == self.response['avg_rate']

