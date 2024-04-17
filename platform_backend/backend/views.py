from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Product, SystemUser
from .serializers import UserSerializer, SysUserSerializer
from rest_framework.views import APIView

# Create your views here.

class ProductListApiView(APIView):
    permission_classes=[permissions.IsAuthenticated]

    #list all
    def get(self, request, *args, **kwags):
        products=Product.objects.filter(user=request.user.id)
        serializer=UserSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #Create
    def post(self, request, *args, **kwargs):
        data={
            'product_name':request.data.get('product_name'),
            'product_price':request.data.get('product_price'),
            'age':request.data.get('age'),
            'user':request.user.id,
            'role':request.data.get('role')
        }
        serializer=UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class SysUserApiView(APIView):
    #LIST ALL
    def get(self, request, *args, **kwargs):
        users=SystemUser.objects
        serializer=SysUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #CREATE
    def post(self, request, *args, **kwargs):
        data={
            'first_name':request.data.get('first_name'),
            'last_name':request.data.get('last_name'),
            'age':request.data.get('age'),
            'email':request.data.get('email'),
            'password':request.data.get('password')
        }
        serializer=SysUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    

    