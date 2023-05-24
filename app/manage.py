


from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from app.models import User, Product, Comment, RecentPrice, UserCollect, UserView, UserValue
from datetime import datetime, timedelta
from random import randint
import random
from django.core.serializers import serialize
from rest_framework import serializers
from app.views import ProductSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'  # 序列化所有字段

# 获取管理信息
def manager_get(request):
    user_information = User.objects.all()
    products_information=Product.objects.all()

    # 序列化商品信息
    serializer_user = UserSerializer(user_information, many=True)
    serialized_user_data = serializer_user.data

    serializer_product = ProductSerializer(products_information, many=True)
    serialized_product_data = serializer_product.data

    # 将序列化后的数据返回给前端
    data = {
        'products': serialized_product_data,
        'user':serialized_user_data
    }
    return JsonResponse(data)
