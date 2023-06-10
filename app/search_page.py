from django.http import JsonResponse
from app.models import Product, UserCollect
from django.db.models import Q
from app.views import ProductSerializer


def get_goods(request, string, user_id, focus=False):
    query = request.GET.get(string)  # 获取关键字
    if focus:   # 若点击了我的关注
        product_id = UserCollect.object.filter(user_id=user_id).values_list('product_id', flat=True)   # 先在我的关注数据库寻找用户关注商品
        products = Product.objects.filter(Q(id__icontains=query), product_id__in=product_id)   # 再在
    else:       # 没有点击我的关注
        products = Product.objects.filter(Q(id__icontains=query))

    # 将序列化后的数据返回给前端
    serializer = ProductSerializer(products, many=True)
    serialized_data = serializer.data
    data = {
        'products': serialized_data
    }

    return JsonResponse(data)

