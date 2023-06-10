from django.http import JsonResponse
from app.models import Product, UserCollect, Comment
from app.views import CommentSerializer

def addfocus(request, user_id, product_id):
    flag = UserCollect.objects.create(user_id=user_id, product_id=product_id)
    if flag:
        return JsonResponse("Add Successfully")
    else:
        return JsonResponse("Add Unsuccessfully")


def getcomments(request, product_id):
    comments = Comment.object.filter(product_id=product_id)
    serializer = CommentSerializer(comments, many=True)
    serialized_data = serializer.data
    data = {
        'comments': serialized_data
    }
    return JsonResponse(data)
