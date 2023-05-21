from django.shortcuts import render, HttpResponse
from app.models import User, Product, Comment, RecentPrice, UserCollect, UserView
from datetime import datetime, timedelta
from random import randint
import random


# Create your views here.
def create(request):
    # 待插入的10条数据

    # user_list = [
    #     User(user_id=i,
    #          user_name=f"User_{i}",
    #          user_wechat=f"wechat_{i}",
    #          phone_number=randint(10000000000, 19999999999))
    #     for i in range(1, 11)  # 假设要创建10个数据记录
    # ]
    #
    # User.objects.bulk_create(user_list)

    # 清理表中的数据，创建时不需要运行这条命令
    # User.objects.all().delete()

    # products_list = [
    #     Product(id=i,
    #             name=f'Product {i}',
    #             image=f'https://example.com/images/product_{i}.jpg',
    #             pics=f'https://example.com/images/product_{i}_1.jpg,https://example.com/images/product_{i}_2.jpg',
    #             price=random.uniform(1, 100),
    #             value=random.randint(1, 100),
    #             notvalue=random.randint(1, 100),
    #             referrer_id=random.randint(1, 10),
    #             recommended_time=datetime.now() - timedelta(days=random.randint(1, 30)),
    #             purchase_method=random.choice(['Online', 'In-store']),
    #             recommendation_reason=f'This product is great for reason {i}',
    #             introduce=f'This is an introduction for Product {i}. It has many features and benefits.'
    #             )
    #     for i in range(1, 11)
    # ]
    #
    # Product.objects.bulk_create(products_list)
    # Product.objects.all().delete()

    # comment_list = [
    #     Comment(user=User.objects.get(user_id=randint(1, 10)),
    #             good_id=Product.objects.get(id=randint(1, 10)),
    #             content=content,
    #             time=datetime.now())
    #     for content in ['This product is amazing!', 'I love this product so much!',
    #                     'This product is not worth the price.', 'I had a bad experience with this product.',
    #                     'This product is not worth the price.', 'This product is this product so much!',
    #                     'This product is not worth the price.', 'I had a bad experience with this product.',
    #                     'This product is not worth the price.', 'This product is this product so much!']
    # ]
    # Comment.objects.bulk_create(comment_list)

    # Comment.objects.all().delete()

    # 待插入的10条数据这部分如果重复运行会报错，因为使用了关联键

    # price_list = [
    #     RecentPrice(
    #         id=Product.objects.get(id=product_id),
    #         price1=random.uniform(10.0, 50.0),
    #         price2=random.uniform(10.0, 50.0),
    #         price3=random.uniform(10.0, 50.0),
    #         price4=random.uniform(10.0, 50.0),
    #         price5=random.uniform(10.0, 50.0),
    #         price6=random.uniform(10.0, 50.0)
    #     )
    #     for product_id in range(1, 11)
    # ]
    #
    # RecentPrice.objects.bulk_create(price_list)

    # RecentPrice.objects.all().delete()

    # 待插入的10条数据

    # 获取可用的 user_id 列表和 product_id 列表
    # user_ids = list(User.objects.values_list('user_id', flat=True))
    # product_ids = list(Product.objects.values_list('id', flat=True))
    #
    # user_collect_list = [
    #     UserCollect(user_id=random.choice(user_ids), product_id=random.choice(product_ids))
    #     for _ in range(1, 11)
    # ]

    # 清空之后需要在命令行执行：alter table app_usercollect AUTO_INCREMENT 1;
    # user_collect_list = [
    #     UserCollect(user_id=User.objects.get(user_id=randint(1, 10)), product_id=Product.objects.get(id=randint(1, 10)))
    #     for _ in range(1, 11)
    # ]
    # UserCollect.objects.bulk_create(user_collect_list)
    # UserCollect.objects.all().delete()

    # 待插入的10条数据
    # user_view_list = [
    #     UserView(user_id=User.objects.get(user_id=randint(1, 10)), product_id=Product.objects.get(id=randint(1, 10)),
    #              time=datetime.now())
    #     for _ in range(1, 11)
    # ]
    # UserView.objects.bulk_create(user_view_list)
    # UserCollect.objects.all().delete()

    return HttpResponse("测试成功")
