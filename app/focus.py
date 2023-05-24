
import json

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from app.models import User, Product, Comment, RecentPrice, UserCollect, UserView, UserValue
from app.views import ProductSerializer
from datetime import datetime, timedelta
from random import randint
import random
from django.core.serializers import serialize

# 获取相似商品信息
def getgoodsList1(request,user_id):
    # 先获取用户收藏的商品的商品名
    user_collect = UserCollect.objects.filter(user_id=user_id)
    product_ids = [collect.product_id for collect in user_collect]

    products = Product.objects.filter(id__in=product_ids)
    product_names= [collect.product_id for collect in products]

    # 查找和用户商品名相同的商品的信息
    similar_goods= []
    for product_name in product_names:
        similar_good = Product.objects.filter(name=product_name)
        similar_goods.append(similar_good)

    # 序列化商品信息
    serializer = ProductSerializer(similar_goods, many=True)
    serialized_data = serializer.data

    # 将序列化后的数据返回给前端
    data = {
        'products': serialized_data
    }
    return JsonResponse(data)