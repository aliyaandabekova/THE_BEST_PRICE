from django.urls import path
from .views import *

urlpatterns = [
    path('register/',RegisterView.as_view()),
    path('profile/',ProfileView.as_view()),
    path('login/',LoginView.as_view()),
    path('score/<int:product_id>/',ScoreView.as_view()),

]