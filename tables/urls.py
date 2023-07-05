from django.urls import path
from . import views

app_name = 'tables'

urlpatterns =[
    path('',views.create,name="create"),
    path('list/',views.list,name="list"),
    path('<int:pk>/',views.detail,name="detail"),
]