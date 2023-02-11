from rest_framework import serializers
from .models import *

class Menu_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['Id', 'Food', 'Price'] 

class Order_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['Id', 'Order', 'Name', 'Price']

class Clients_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['Id', 'Name']