from django.urls import path
from . import views

app_name = 'dashboards'

urlpatterns = [
    path('',views.create,name="create"),
    path('new/',views.new,name="new"),
    path('<int:pk>/',views.detail,name="detail"),
    path('<int:pk>/update/',views.update,name="update"),
    path('delete/<int:pk>/',views.delete,name="delete"),
]