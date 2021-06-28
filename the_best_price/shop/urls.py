from django.urls import path
from .views import *

urlpatterns = [
    path('score/<str:shop_name>/', ShopScoreView.as_view(),name='shop_score'),
    path('shops/',ShopsView.as_view()),
    path('comment/<str:shop_name>/',CommentView.as_view()),

]