

import json

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from app.models import User, Product, Comment, RecentPrice, UserCollect, UserView, UserValue
from app.views import ProductSerializer
from datetime import datetime, timedelta
from random import randint
import random
from django.core.serializers import serialize


# 提交爆料
def submit_break(request):
    post_data = request.body
    # JSON数据转换成Python数据类型
    data = json.loads(post_data)
    # 根据需要获取指定数据
    id_ = data['id']
    name_ = data['name']
    image_ = data['image']
    pics_ = data['pics']
    price_ = data['price']
    value_ = data['value']
    notvalue_ = data['notvalue']
    referrer_id_ = data['referrer_id']
    recommended_time_ = data['recommended_time']
    purchase_method_ = data['purchase_method']
    recommendation_reason_ = data['recommendation_reason']
    recent_prices_ = data['recent_prices']
    introduce_ = data['introduce']
    products = [
        Product(id=id_, name=name_,image=image_,pics=pics_,price=price_,value=value_,notvalue=notvalue_,referrer_id=referrer_id_,
                recommended_time=recommended_time_,purchase_method=purchase_method_,recommendation_reason=recommendation_reason_,
                recent_prices=recent_prices_,introduce=introduce_)
    ]
    # 插入爆料数据
    if_success = Product.objects.bulk_create(products);

    if if_success:
        return True
    else:
        return False