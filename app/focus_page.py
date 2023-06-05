from django.http import JsonResponse
from app.models import Product, UserCollect


def userfocus(request, user_id):
    # 先在我的关注中寻找某个用户的关注商品id
    product_id = UserCollect.object.filter(user_id=user_id).values_list('product_id', flat=True)
    products = Product.object.filter(product_id__in=product_id)     # 再在商品数据库中寻找商品
    data = {
        'products': products
    }
    return JsonResponse(data)


def userdelete(request, user_id, product_id):
    flag = UserCollect.objects.filter(user_id=user_id, id=product_id).delete() # 直接删除某个用户的关注的某个商品的id
    if flag:
        return JsonResponse("Delete Successfully")
    else:
        return JsonResponse("Delete Unsuccessfully")

