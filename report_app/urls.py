import imp
from django.urls import path

from .views import listOfOrders

urlpatterns = [
    path('orderList',listOfOrders, name='orderList')
]