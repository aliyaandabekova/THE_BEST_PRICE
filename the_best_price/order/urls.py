from django.urls import path
from .views import *

urlpatterns = [
    path('my_orders/',MyOrderView.as_view()),

]