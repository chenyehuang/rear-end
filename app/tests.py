from django.test import TestCase
from django.test import TestCase, Client
from app.models import User, Product, Comment, UserCollect, UserView, UserValue
# Create your tests here.
# 对于数据库中的表的增删改查测试
# class ProjectTest(TestCase):

#     def setUp(self) -> None:
#         self.client = Client()
#         User.objects.create(openid="test_id", nickName="测试", avatarUrl="test_url")
        # self.product={
        #         'id': 11,
        #         'name': '笔记本礼盒套装2023年新款笔记本套装定制logo',
        #         'image': 'http://47.115.221.21:8081/pic/goods/goods1.png',
        #         'pics': ['http://47.115.221.21:8081/pic/goods/goods1-1.png', 'http://47.115.221.21:8081/pic/goods/goods1-2.png',
        #                     'http://47.115.221.21:8081/pic/goods/goods1-3.png'],
        #         'price': 28.8,
        #         'value': 90,
        #         'notvalue': 118,
        #         'referrer_id': "test_id",
        #         'recommended_time': '2023-05-19T12:34:56',
        #         'purchase_method': '淘宝',
        #         'recommendation_reason': '因为比较便宜且实用',
        #         'recent_prices': [
        #             {'price': 29.9, 'time': '2023-04-10'},
        #             {'price': 31.2, 'time': '2023-04-20'},
        #             {'price': 23.3, 'time': '2023-04-30'},
        #             {'price': 40.0, 'time': '2023-05-10'},
        #             {'price': 29.9, 'time': '2023-05-15'},
        #             {'price': 28.8, 'time': '2023-05-20'}
        #         ],
        #         'introduce': '笔记本礼盒套装2023年新款笔记本套装定制logo笔记本定制logo印字国潮笔记本礼盒学生奖品礼品笔记本可印logo，品牌：CTFP/楚天飞鹏型号：窗花本山水情风格：复古风 '
        #                         '商务品牌：CTFP/楚天飞鹏型号：窗花本山水情风格：复古风 商务 包装数量：单本装封面材质：仿皮生产企业：楚天飞鹏 封面硬度：硬面抄幅面：A5记事本分类：通用笔记本 '
        #                         '装订方式：线装式装订适用人群：商务办公人士 通用内页材质：道林纸 '
        # }
#         Product(**self.product)
#         # user = User.objects.get(openid="test_id")
        # product = Product.objects.get(id=11)
        # UserCollect.objects.create(user_id=user, product_id=product)

    # def test_create(self):
    #     p = Product.objects.get(id=11)
    #     self.assertEqual(p.name, '笔记本礼盒套装2023年新款笔记本套装定制logo')

    # def test_delete(self):
    #     p = Department.objects.get(title="测试")
    #     p.delete()
    #     ret = Department.objects.filter(title="测试")
    #     self.assertEqual(len(ret), 0)

    # def test_update(self):
    #     p = Department.objects.get(title="测试")
    #     p.title = "测试3"
    #     p.save()

    #     ret = Department.objects.get(title="测试3")
    #     self.assertEqual(ret.title, "测试3")

    # def test_index_url(self):
    #     response = self.client.get("/user/list")
    #     print(response.status_code)
    #     self.assertEqual(response.status_code, 200)

class ProductTest(TestCase):
    def setUp(self):
        # 创建测试数据
        self.product_data = {
                'id': 11,
                'name': '笔记本礼盒套装2023年新款笔记本套装定制logo',
                'image': 'http://47.115.221.21:8081/pic/goods/goods1.png',
                'pics': ['http://47.115.221.21:8081/pic/goods/goods1-1.png', 'http://47.115.221.21:8081/pic/goods/goods1-2.png',
                            'http://47.115.221.21:8081/pic/goods/goods1-3.png'],
                'price': 28.8,
                'value': 90,
                'notvalue': 118,
                'referrer_id': "test_id",
                'recommended_time': '2023-05-19T12:34:56',
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
        }

    def test_create_product(self):
        # 创建产品
        product = Product.objects.create(**self.product_data)
        
        # 断言产品已成功创建
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(product.name, '笔记本礼盒套装2023年新款笔记本套装定制logo')

    def test_update_product(self):
        # 创建产品
        product = Product.objects.create(**self.product_data)
        
        # 更新产品信息
        product.name = 'Updated Product'
        product.save()

        # 断言产品信息已成功更新
        updated_product = Product.objects.get(pk=product.pk)
        self.assertEqual(updated_product.name, 'Updated Product')

    def test_delete_product(self):
        # 创建产品
        product = Product.objects.create(**self.product_data)

        # 删除产品
        product.delete()

        # 断言产品已成功删除
        self.assertEqual(Product.objects.count(), 0)

    def test_retrieve_product(self):
        # 创建产品
        product = Product.objects.create(**self.product_data)

        # 获取产品信息
        retrieved_product = Product.objects.get(pk=product.pk)

        # 断言获取的产品信息正确
        self.assertEqual(retrieved_product.name, '笔记本礼盒套装2023年新款笔记本套装定制logo')

# URL路由测试
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

class URLRoutingTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        User.objects.create(openid='test_openid', nickName='Test_User', avatarUrl="test_url")
        # self.product_data_test = {
        #         'id': 1,
        #         'name': '笔记本礼盒套装2023年新款笔记本套装定制logo',
        #         'image': 'http://47.115.221.21:8081/pic/goods/goods1.png',
        #         'pics': ['http://47.115.221.21:8081/pic/goods/goods1-1.png', 'http://47.115.221.21:8081/pic/goods/goods1-2.png',
        #                     'http://47.115.221.21:8081/pic/goods/goods1-3.png'],
        #         'price': 28.8,
        #         'value': 90,
        #         'notvalue': 118,
        #         'referrer_id': "test_id",
        #         'recommended_time': '2023-05-19T12:34:56',
        #         'purchase_method': '淘宝',
        #         'recommendation_reason': '因为比较便宜且实用',
        #         'recent_prices': [
        #             {'price': 29.9, 'time': '2023-04-10'},
        #             {'price': 31.2, 'time': '2023-04-20'},
        #             {'price': 23.3, 'time': '2023-04-30'},
        #             {'price': 40.0, 'time': '2023-05-10'},
        #             {'price': 29.9, 'time': '2023-05-15'},
        #             {'price': 28.8, 'time': '2023-05-20'}
        #         ],
        #         'introduce': '笔记本礼盒套装2023年新款笔记本套装定制logo笔记本定制logo印字国潮笔记本礼盒学生奖品礼品笔记本可印logo，品牌：CTFP/楚天飞鹏型号：窗花本山水情风格：复古风 '
        #                         '商务品牌：CTFP/楚天飞鹏型号：窗花本山水情风格：复古风 商务 包装数量：单本装封面材质：仿皮生产企业：楚天飞鹏 封面硬度：硬面抄幅面：A5记事本分类：通用笔记本 '
        #                         '装订方式：线装式装订适用人群：商务办公人士 通用内页材质：道林纸 '
        # }
        Product.objects.create(id=1, name="test_product", image="test_image", pics=["test_pics"], 
                               price=10, value=20, notvalue=30, referrer_id="test_openid", recommended_time=timezone.datetime(2023, 6, 1, 10, 30),
                               purchase_method='test_channel', recommendation_reason="test_reason",
                               recent_prices=[{'price':50, 'time':"test_recent_time"}], introduce="test_introduce")
    def test_get_product_url(self):
        url = reverse('get_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_get_user_url(self):
        url = reverse('get_user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_get_product_detail_url(self):
        product_id = 1  # Replace with an actual product ID
        url = reverse('get_product_detail', args=[product_id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_get_product_new_url(self):
        url = reverse('get_product_new')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_get_product_hot_url(self):
        url = reverse('get_product_hot')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_create_user_url(self):
        url = reverse('create_user')
        response = self.client.post(url, {'username': 'test_user', 'password': 'test_password'})
        self.assertEqual(response.status_code, 200)
    
    def test_get_front_product_url(self):
        url = reverse('get_front_product')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_search_products_url(self):
        url = reverse('search_products')
        response = self.client.get(url, {'query': 'test_query'})
        self.assertEqual(response.status_code, 200)
    
    def test_add_collect_url(self):
        url = reverse('add_collect')
        response = self.client.post(url, {'user_id': 1, 'product_id': 1})
        self.assertEqual(response.status_code, 200)
    
    def test_delete_collect_url(self):
        url = reverse('delete_collect')
        response = self.client.post(url, {'user_id': 1, 'product_id': 1})
        self.assertEqual(response.status_code, 200)
    
    def test_get_product_pic_url(self):
        url = reverse('get_product_pic')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_get_user_comment_url(self):
        url = reverse('get_user_comment')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_add_comment_url(self):
        url = reverse('add_comment')
        response = self.client.post(url, {'user_id': 1, 'product_id': 1, 'content': 'Test comment'})
        self.assertEqual(response.status_code, 200)
    
    def test_get_user_collect_url(self):
        openid = 'test_openid'
        url = reverse('get_user_collect', args=[openid])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def test_get_product_comment_url(self):
        product = Product.objects.get(id=1)  # 创建一个产品对象
        url = reverse('get_product_comment')
        response = self.client.get(url, {'good_id': product.id})  # 传递产品ID作为参数
        self.assertEqual(response.status_code, 200)
    
    def test_add_product_url(self):
        url = reverse('add_product')
        response = self.client.post(url, {'name': 'Test Product', 'price': 10.99})
        self.assertEqual(response.status_code, 200)
    
    def test_delete_user_url(self):
        url = reverse('delete_user')
        response = self.client.post(url, {'user_id': 1})
        self.assertEqual(response.status_code, 200)
    
    def test_delete_product_url(self):
        url = reverse('delete_product')
        response = self.client.post(url, {'product_id': 1})
        self.assertEqual(response.status_code, 200)
    
    def test_delete_manage_comment_url(self):
        user = User.objects.get(openid="test_openid")  # 创建一个用户对象
        product = Product.objects.get(id=1)
        content = "test_content"
        url = reverse('delete_manage_comment')
        response = self.client.get(url, {'openid': user.openid, "product_id":product.id, "content":content})  # 传递用户openid作为参数
        self.assertEqual(response.status_code, 200)

