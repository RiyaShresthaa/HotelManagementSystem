from rest_framework import serializers
from .models import *

class RoomTypeSerializer(serializers.ModelSerializer):#inherite modelserializer from serializer 
    class Meta:#meta class defined can extra features of class
        model = RoomType
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerDetail
        fields = "__all__"

class BillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bill
        fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"

class EmployeeInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeInfo
        fields = "__all__"

class MenuTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuType
        fields = "__all__"

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = "__all__"

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = "__all__"