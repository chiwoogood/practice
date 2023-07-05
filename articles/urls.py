from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index),
    path('welcome/<name>/',views.welcome),
    path('fakelove/',views.fakelove),
    path('ping/',views.ping),
    path('pong/',views.pong),
]