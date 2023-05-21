import json

from django.http import JsonResponse
from django.shortcuts import render, HttpResponse
from app.models import User, Product, Comment, RecentPrice, UserCollect, UserView, UserValue
from datetime import datetime, timedelta
from random import randint
import random
from django.core.serializers import serialize
from rest_framework import serializers


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

    """    products_list = [
        {
            'id': 1,
            'name': '笔记本礼盒套装2023年新款笔记本套装定制logo',
            'image': '../../image/goods/goods1.png',
            'pics': ['../../image/goods/goods1-1.png', '../../image/goods/goods1-2.png',
                     '../../image/goods/goods1-3.png'],
            'price': 28.8,
            'value': 90,
            'notvalue': 118,
            'referrer_id': 1,
            'recommended_time': '2023-05-19T12:34:56',  # 根据实际日期时间格式进行调整
            'purchase_method': '淘宝',
            'recommendation_reason': '因为比较便宜且实用',
            'recent_prices': [
                {'price': 29.9, 'time': '2023-04-10'},
                {'price': 31.2, 'time': '2023-04-20'},
                {'price': 23.3, 'time': '2023-04-30'},
                {'price': 40.0, 'time': '2023-05-10'},
                {'price': 29.9, 'time': '2023-05-15'},
                {'price': 28.8, 'time': '2023-05-20'}
            ],
            'introduce': '笔记本礼盒套装2023年新款笔记本套装定制logo笔记本定制logo印字国潮笔记本礼盒学生奖品礼品笔记本可印logo，品牌：CTFP/楚天飞鹏型号：窗花本山水情风格：复古风 '
                         '商务品牌：CTFP/楚天飞鹏型号：窗花本山水情风格：复古风 商务 包装数量：单本装封面材质：仿皮生产企业：楚天飞鹏 封面硬度：硬面抄幅面：A5记事本分类：通用笔记本 '
                         '装订方式：线装式装订适用人群：商务办公人士 通用内页材质：道林纸 '
        },
        {
            'id': 2,
            'name': '得力线圈本笔记本考研本子',
            'image': '../../image/goods/goods2.png',
            'pics': ['../../image/goods/goods2-1.png', '../../image/goods/goods2-2.png',
                     '../../image/goods/goods2-3.png'],
            'price': 7.6,
            'value': 190,
            'notvalue': 18,
            'referrer_id': 2,
            'recommended_time': '2023-05-14T12:34:56',  # 根据实际日期时间格式进行调整
            'purchase_method': '淘宝',
            'recommendation_reason': '相当便宜，日常耐用',
            'recent_prices': [
                {'price': 7.6, 'time': '2023-04-10'},
                {'price': 6.8, 'time': '2023-04-20'},
                {'price': 9.9, 'time': '2023-04-30'},
                {'price': 5.5, 'time': '2023-05-10'},
                {'price': 6.8, 'time': '2023-05-15'},
                {'price': 7.6, 'time': '2023-05-20'}

            ],
            'introduce': '得力线圈本笔记本考研本子横线b5学生加厚网格日记本定制文具超厚方格记事本a4本子高中生记录本错题摘抄本，品牌：Deli/得力文具类目型号：线圈本风格：小清新 简约 自然 '
                         '生产企业：得力 适用场景：书写幅面：B5记事本分类：通用笔记本 装订方式：线圈/螺旋适用人群：学生 通用上市时间：2018-04-23 内页材质：道林纸 '
        },
        {
            'id': 3,
            'name': '长尾夹彩色大中小号黑色燕尾夹',
            'image': '../../image/goods/goods3.png',
            'pics': ['../../image/goods/goods3-1.png', '../../image/goods/goods3-2.png',
                     '../../image/goods/goods3-3.png'],
            'price': 5.8,
            'value': 100,
            'notvalue': 15,
            'referrer_id': 3,
            'recommended_time': '2023-05-12T12:34:56',  # 根据实际日期时间格式进行调整
            'purchase_method': '淘宝',
            'recommendation_reason': '日常生活中很多地方都用的到',
            'recent_prices': [
                {'price': 5.8, 'time': '2023-04-10'},
                {'price': 4.9, 'time': '2023-04-20'},
                {'price': 6.6, 'time': '2023-04-30'},
                {'price': 4.8, 'time': '2023-05-10'},
                {'price': 4.9, 'time': '2023-05-15'},
                {'price': 5.8, 'time': '2023-05-20'}

            ],
            'introduce': '长尾夹彩色大中小号黑色燕尾夹文件夹子学生用书夹子试卷夹办公用品文具大全金属小票固定夹子办公室票夹批发，炫彩多功能长尾夹，四色混合装，强劲夹力'
        },

        {
            'id': 4,
            'name': '金属文件架桌面文件收纳盒',
            'image': '../../image/goods/goods4.png',
            'pics': ['../../image/goods/goods4-1.png', '../../image/goods/goods4-2.png',
                     '../../image/goods/goods4-3.png'],
            'price': 26.9,
            'value': 48,
            'notvalue': 128,
            'referrer_id': 4,
            'recommended_time': '2023-05-11T12:34:56',  # 根据实际日期时间格式进行调整
            'purchase_method': '淘宝',
            'recommendation_reason': '放在寝室书桌上方便取东西',
            'recent_prices': [
                {'price': 29.9, 'time': '2023-04-10'},
                {'price': 31.2, 'time': '2023-04-20'},
                {'price': 23.3, 'time': '2023-04-30'},
                {'price': 26.8, 'time': '2023-05-10'},
                {'price': 29.9, 'time': '2023-05-15'},
                {'price': 26.9, 'time': '2023-05-20'}

            ],
            'introduce': '金属文件架桌面文件收纳盒文件框置物架办公用品大全多层档案资料分类立式书架办公桌铁质书立架文件夹架子，镂空设计彰显现代感，'
                         '实心多线条，巧妙分解几面压力。远离杂乱空间，多层次收纳，叠加设计，减少空间，自由组合任意加高，做自己的设计师。 '
        },

        {
            'id': 5,
            'name': '最生活小米毛巾',
            'image': '../../image/goods/goods5.png',
            'pics': ['../../image/goods/goods5-1.png', '../../image/goods/goods5-2.png',
                     '../../image/goods/goods5-3.png'],
            'price': 19.9,
            'value': 230,
            'notvalue': 45,
            'referrer_id': 5,
            'recommended_time': '2023-05-09T12:34:56',  # 根据实际日期时间格式进行调整
            'purchase_method': '淘宝',
            'recommendation_reason': '日常用品，不掉毛很好用',
            'recent_prices': [
                {'price': 29.9, 'time': '2023-04-10'},
                {'price': 23.5, 'time': '2023-04-20'},
                {'price': 23.3, 'time': '2023-04-30'},
                {'price': 25.0, 'time': '2023-05-10'},
                {'price': 15.0, 'time': '2023-05-15'},
                {'price': 19.9, 'time': '2023-05-20'}

            ],
            'introduce': '最生活小米毛巾纯棉洗脸家用不掉毛男士女洗澡吸水新疆棉面巾抗菌。符合年轻人的生活美学，轻柔易干，3'
                         '秒吸水，不仅满足日常的擦手擦脸，而且容易晾干。天生柔软，天然棉花的呵护，不含致癌芳香胺。避免面部尴尬，亲肤不易掉毛，密封包装，即拆即用，轻薄小巧更便携。 '
        },

        {
            'id': 6,
            'name': '海盐持久留香洗手液',
            'image': '../../image/goods/goods6.png',
            'pics': ['../../image/goods/goods6-1.png', '../../image/goods/goods6-2.png',
                     '../../image/goods/goods6-3.png'],
            'price': 15.5,
            'value': 20,
            'notvalue': 113,
            'referrer_id': 6,
            'recommended_time': '2023-05-15T12:34:56',  # 根据实际日期时间格式进行调整
            'purchase_method': '淘宝',
            'recommendation_reason': '香味很好闻，洗完之后很干净',
            'recent_prices': [
                {'price': 20.1, 'time': '2023-04-10'},
                {'price': 16.9, 'time': '2023-04-20'},
                {'price': 18.8, 'time': '2023-04-30'},
                {'price': 20.0, 'time': '2023-05-10'},
                {'price': 15.5, 'time': '2023-05-15'},
                {'price': 15.5, 'time': '2023-05-20'}

            ],
            'introduce': '小红书推荐海盐持久留香洗手液家用抑菌保湿滋润不伤手儿童可用，海盐洗手液清爽洁净手部油脂和污垢。'
                         '温和配方不刺激双手，多种香氛呵护双手，细腻泡沫捕捉每个污渍角落。'
        },

        {
            'id': 7,
            'name': '晾衣架落地卧室可移动家用晾衣架',
            'image': '../../image/goods/goods7.png',
            'pics': ['../../image/goods/goods7-1.png', '../../image/goods/goods7-2.png',
                     '../../image/goods/goods7-3.png'],
            'price': 56.0,
            'value': 36,
            'notvalue': 125,
            'referrer_id': 7,
            'recommended_time': '2023-05-11T11:34:56',  # 根据实际日期时间格式进行调整
            'purchase_method': '淘宝',
            'recommendation_reason': '很实用，衣服放着不褶皱',
            'recent_prices': [
                {'price': 60.2, 'time': '2023-04-10'},
                {'price': 59.8, 'time': '2023-04-20'},
                {'price': 59.9, 'time': '2023-04-30'},
                {'price': 40.0, 'time': '2023-05-10'},
                {'price': 56.3, 'time': '2023-05-15'},
                {'price': 56.0, 'time': '2023-05-20'}

            ],
            'introduce': '晾衣架落地卧室可移动家用晾衣架阳台挂衣服架子室内简易单杆衣架,多功能分区收纳，收纳衣物快速寻找'
        },

        {
            'id': 8,
            'name': 'SukGarden樱花洗衣液进口香氛',
            'image': '../../image/goods/goods8.png',
            'pics': ['../../image/goods/goods8-1.png', '../../image/goods/goods8-2.png',
                     '../../image/goods/goods8-3.png'],
            'price': 99.9,
            'value': 12,
            'notvalue': 118,
            'referrer_id': 8,
            'recommended_time': '2023-05-17T11:34:56',  # 根据实际日期时间格式进行调整
            'purchase_method': '淘宝',
            'recommendation_reason': '用这个洗衣服特别香',
            'recent_prices': [
                {'price': 108.4, 'time': '2023-04-10'},
                {'price': 99.9, 'time': '2023-04-20'},
                {'price': 100.0, 'time': '2023-04-30'},
                {'price': 102.3, 'time': '2023-05-10'},
                {'price': 98.9, 'time': '2023-05-15'},
                {'price': 100.0, 'time': '2023-05-20'}

            ],
            'introduce': '樱花洗衣液进口香氛男女士持久留香整箱批补充袋装家用 1件装，生态配方，创新升级，创新纳米爆香科技，500倍清洁力，椰油精华，抗菌除螨。'
        },

        {
            'id': 9,
            'name': 'meyarn米妍正畸牙膏',
            'image': '../../image/goods/goods9.png',
            'pics': ['../../image/goods/goods9-1.png', '../../image/goods/goods9-2.png',
                     '../../image/goods/goods9-3.png'],
            'price': 35.9,
            'value': 112,
            'notvalue': 13,
            'referrer_id': 9,
            'recommended_time': '2023-05-12T16:34:56',  # 根据实际日期时间格式进行调整
            'purchase_method': '淘宝',
            'recommendation_reason': '很好用，保护牙齿',
            'recent_prices': [
                {'price': 36.2, 'time': '2023-04-10'},
                {'price': 31.2, 'time': '2023-04-20'},
                {'price': 30.2, 'time': '2023-04-30'},
                {'price': 36.5, 'time': '2023-05-10'},
                {'price': 35.9, 'time': '2023-05-15'},
                {'price': 35.9, 'time': '2023-05-20'}

            ],
            'introduce': 'meyarn米妍正畸牙膏含氟清新口气预防蛀牙龋齿带牙套专用便携牙膏，1450ppm高滞留氟配方，防止虫蛀。'
        },

        {
            'id': 10,
            'name': '家用电脑椅子网红简约透明凳子',
            'image': '../../image/goods/goods10.png',
            'pics': ['../../image/goods/goods10-1.png', '../../image/goods/goods10-2.png',
                     '../../image/goods/goods10-3.png'],
            'price': 111.2,
            'value': 58,
            'notvalue': 156,
            'referrer_id': 10,
            'recommended_time': '2023-05-11T16:34:56',  # 根据实际日期时间格式进行调整
            'purchase_method': '淘宝',
            'recommendation_reason': '很好用，保护牙齿',
            'recent_prices': [
                {'price': 100.9, 'time': '2023-04-10'},
                {'price': 132.0, 'time': '2023-04-20'},
                {'price': 119.2, 'time': '2023-04-30'},
                {'price': 102.3, 'time': '2023-05-10'},
                {'price': 110.0, 'time': '2023-05-15'},
                {'price': 111.2, 'time': '2023-05-20'}

            ],
            'introduce': '家用电脑椅子网红简约透明凳子卧室书房旋转升降靠背椅办公学习椅，品牌：麦田型号：YJXYZ0001是否可定制：否 是否可升降：是是否可旋转：是是否可躺：否 '
                         '五星脚材质：尼龙脚扶手类型：无扶手是否支持人体工程学：是 产地：浙江省是否组装：是包装体积：袋装 出租车是否可运输：是款式定位：经济型安装说明详情：提供安装说明书 提供安装说明视频 '
                         '提供简单安装工具 毛重：6kg是否带脚踏：否 '
        },

    ]

    Product.objects.bulk_create([
        Product(**data) for data in products_list
    ])"""

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
    # alter table app_userview AUTO_INCREMENT 1;
    # user_view_list = [
    #     UserView(user_id=User.objects.get(user_id=randint(1, 10)), product_id=Product.objects.get(id=randint(1, 10)),
    #              time=datetime.now())
    #     for _ in range(1, 11)
    # ]
    # UserView.objects.bulk_create(user_view_list)
    # UserCollect.objects.all().delete()

    # alter table app_uservalue AUTO_INCREMENT 1;
    # user_value_list = [
    #     UserValue(user_id=User.objects.get(user_id=randint(1, 10)), product_id=Product.objects.get(id=randint(1, 10)),
    #               value_or_not=randint(0, 1))
    #     for _ in range(1, 11)
    # ]

    # UserValue.objects.bulk_create(user_value_list)
    # UserValue.objects.all().delete()

    return HttpResponse("创建成功")


# 序列化商品数据
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # 序列化所有字段


# 序列化评论数据
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'  # 序列化所有字段


# 获取用户收藏
def get_user_collect(request, user_id):
    user_collect = UserCollect.objects.filter(user_id=user_id)
    product_ids = [collect.product_id_id for collect in user_collect]
    products = Product.objects.filter(id__in=product_ids)

    # 序列化商品信息
    serializer = ProductSerializer(products, many=True)
    serialized_data = serializer.data

    # 将序列化后的数据返回给前端
    data = {
        'products': serialized_data
    }

    return JsonResponse(data)


# 获取用户值/不值
def get_user_value(request, user_id, value_flag):
    user_value = UserValue.objects.filter(user_id=user_id, value_or_not=value_flag)
    product_ids = [collect.product_id_id for collect in user_value]
    products = Product.objects.filter(id__in=product_ids)

    # 序列化商品信息
    serializer = ProductSerializer(products, many=True)
    serialized_data = serializer.data

    # 将序列化后的数据返回给前端
    data = {
        'products': serialized_data
    }

    return JsonResponse(data)


# 用户最新爆料
def get_user_new_break(request, user_id):
    user_new_break = Product.objects.filter(referrer_id=user_id)
    # 按时间从新到旧排序
    products = user_new_break.order_by('-recommended_time')

    # 序列化商品信息
    serializer = ProductSerializer(products, many=True)
    serialized_data = serializer.data

    # 将序列化后的数据返回给前端
    data = {
        'products': serialized_data
    }

    return JsonResponse(data)


# 用户最热爆料
def get_user_hot_break(request, user_id):
    user_hot_break = Product.objects.filter(referrer_id=user_id)
    # 按热度从高到低排序
    products = user_hot_break.order_by('-value')

    # 序列化商品信息
    serializer = ProductSerializer(products, many=True)
    serialized_data = serializer.data

    # 将序列化后的数据返回给前端
    data = {
        'products': serialized_data
    }

    return JsonResponse(data)


# 用户发出的评论
def get_make_comment(request, user_id):
    user_make_comment = Comment.objects.filter(user=user_id)
    serializer = CommentSerializer(user_make_comment, many=True)
    serialized_data = serializer.data

    # 将序列化后的数据返回给前端
    data = {
        'comments': serialized_data
    }

    return JsonResponse(data)


# 用户收到的评论
def get_comment(request, user_id):
    product_comment = Product.objects.filter(referrer_id=user_id)
    product_ids = [collect.id for collect in product_comment]
    user_get_comment = Comment.objects.filter(good_id__in=product_ids)
    serializer = CommentSerializer(user_get_comment, many=True)
    serialized_data = serializer.data

    # 将序列化后的数据返回给前端
    data = {
        'comments': serialized_data
    }

    return JsonResponse(data)


# 用户最热排序的浏览记录
def history_hot_product(request, user_id):
    user_view = UserView.objects.filter(user_id=user_id)
    product_ids = [collect.product_id for collect in user_view]
    products = Product.objects.filter(id__in=product_ids).order_by('-value')
    # 序列化商品信息
    serializer = ProductSerializer(products, many=True)
    serialized_data = serializer.data

    # 将序列化后的数据返回给前端
    data = {
        'products': serialized_data
    }

    return JsonResponse(data)


# 用户最新排序的浏览记录
def history_new_product(request, user_id):
    user_view = UserView.objects.filter(user_id=user_id)
    product_ids = [collect.product_id for collect in user_view]
    products = Product.objects.filter(id__in=product_ids).order_by('-recommended_time')
    # 序列化商品信息
    serializer = ProductSerializer(products, many=True)
    serialized_data = serializer.data

    # 将序列化后的数据返回给前端
    data = {
        'products': serialized_data
    }

    return JsonResponse(data)
