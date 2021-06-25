from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from product.models import *
from userprofile.models import *
from order.models import *

class ScoreTest(APITestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(name='dress', price=400, score_from_api=3.0)
        self.user = User.objects.create_user(username='aliya',password='123456')
        self.profile = Profile.objects.create(user=self.user,full_name='aliyaaaaa')
        self.order = Order.objects.create(profile=self.profile,product=self.product)
        self.url = reverse('score', args=(self.product.id,))
    def test_score_post(self):
        self.client.login(username='aliya',password='123456')
        data = {
            "score":4
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code, 201)



class ScoreTest(APITestCase):
    def setUp(self) -> None:
        self.product = Product.objects.create(name='dress', price=400, score_from_api=3.0)
        self.user = User.objects.create_user(username='aliya',password='123456')
        self.profile = Profile.objects.create(user=self.user,full_name='aliyaaaaa')
        self.url = reverse('score', args=(self.product.id,))
    def test_score_post_bad_order(self):
        self.client.login(username='aliya',password='123456')
        data = {
            "score":4
        }
        self.response = self.client.post(self.url,data)
        self.assertEqual(self.response.status_code, 404)