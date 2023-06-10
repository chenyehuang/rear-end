from django.http import JsonResponse
from app.models import Product
from django.db.models import Q
import random
from app.views import ProductSerializer


def getpicgoods(request, query):
    random_list = [random.randint(1, 10) for i in range(3)]    # 制作长度为3的随机数列表
    product_data = Product.objects.filter(id__in=random_list)   # 获取id号为列表中数据的商品数据

    serializer = ProductSerializer(product_data, many=True)
    serialized_data = serializer.data
    data = {
        'products': serialized_data
    }
    return JsonResponse(data)


def getrank(request, query):
    query = request.GET.get(query)      # 获取关键字
    products = Product.object.all().order_by('-'+query)     # 按关键字降序排序
    serializer = ProductSerializer(products, many=True)     # 获取降序后的数据

    serialized_data = serializer.data
    data = {
        'products': serialized_data
    }
    return JsonResponse(data)