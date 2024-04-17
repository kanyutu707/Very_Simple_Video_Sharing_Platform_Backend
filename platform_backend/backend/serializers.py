from rest_framework import serializers
from .models import Product, SystemUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=["product_name", "product_price", "age", "role", "user"]

class SysUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=SystemUser
        fields=["first_name", "last_name", "age", "email", "password"]