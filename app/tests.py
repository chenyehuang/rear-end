from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from app.models import User, Product, Comment, UserCollect, UserView, UserValue
from django.db.models import Q
from django.db.models.functions import Random
from app.views import ProductSerializer, CommentSerializer, UserSerializer
import datetime
import dateutil.parser

# Create your tests here.

# URL路由测试
class URLRoutingTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        User.objects.create(openid='test_openid', nickName='Test_User', avatarUrl="test_url")
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

    def test_value_or_not_url(self):
        url = reverse('value_or_not')
        response = self.client.post(url, {'openid': 'your_openid', 'goodInfo': 'your_good_info', 'value': 1})
        self.assertEqual(response.status_code, 200)

    def test_get_user_value_url(self):
        url = reverse('get_user_value')
        response = self.client.get(url, {'openid': "test_openid"})
        self.assertEqual(response.status_code, 200)


#对数据表的测试
class ModelTestCase(TestCase):
    def setUp(self) -> None:
        self.client = Client()
        User.objects.create(openid='test_openid', nickName='Test_User', avatarUrl="test_url")
        Product.objects.create(id=1, name="test_product", image="test_image", pics=["test_pics"], 
                               price=10, value=20, notvalue=30, referrer_id="test_openid", recommended_time=timezone.datetime(2023, 6, 1, 10, 30),
                               purchase_method='test_channel', recommendation_reason="test_reason",
                               recent_prices=[{'price':50, 'time':"test_recent_time"}], introduce="test_introduce")
    
    def test_user_model(self):
        User.objects.all().delete()
        user = User.objects.create(openid='test_openid', nickName='Test User', avatarUrl='test_avatar')
        self.assertEqual(user.openid, 'test_openid')
        self.assertEqual(user.nickName, 'Test User')
        self.assertEqual(user.avatarUrl, 'test_avatar')
        # Read
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get(openid='test_openid'), user)
        
        # Update
        user.nickName = 'Updated User'
        user.save()
        self.assertEqual(User.objects.get(openid='test_openid').nickName, 'Updated User')
        
        # Delete
        user.delete()
        self.assertEqual(User.objects.count(), 0)


    def test_product_model(self):
        Product.objects.all().delete()
        product = Product.objects.create(id=11, name="test_product", image="test_image", pics=["test_pics"], 
                               price=10, value=20, notvalue=30, referrer_id="test_openid", recommended_time=timezone.datetime(2023, 6, 1, 10, 30),
                               purchase_method='test_channel', recommendation_reason="test_reason",
                               recent_prices=[{'price':50, 'time':"test_recent_time"}], introduce="test_introduce")
        self.assertEqual(product.name, 'test_product')
        self.assertEqual(product.price, 10)

         # Read
        self.assertEqual(Product.objects.count(), 1)
        self.assertEqual(Product.objects.get(name='test_product'), product)
        
        # Update
        product.name = 'Updated Product'
        product.save()
        self.assertEqual(Product.objects.get(name='Updated Product').price, 10)
        
        # Delete
        product.delete()
        self.assertEqual(Product.objects.count(), 0)
    
    def test_comment_model(self):
        user = User.objects.get(openid='test_openid')
        product = Product.objects.get(id=1)
        comment = Comment.objects.create(user=user, good_id=product, content='Test Comment')
        self.assertEqual(comment.user, user)
        self.assertEqual(comment.good_id, product)
        self.assertEqual(comment.content, 'Test Comment')

        # Read
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(Comment.objects.get(content='Test Comment'), comment)
        
        # Update
        comment.content = 'Updated Comment'
        comment.save()
        self.assertEqual(Comment.objects.get(content='Updated Comment').user, user)
        
        # Delete
        comment.delete()
        self.assertEqual(Comment.objects.count(), 0)
    
    def test_user_collect_model(self):
        user = User.objects.get(openid='test_openid')
        product = Product.objects.get(id=1)
        user_collect = UserCollect.objects.create(user_id=user, product_id=product)
        self.assertEqual(user_collect.user_id, user)
        self.assertEqual(user_collect.product_id, product)

        # Read
        self.assertEqual(UserCollect.objects.count(), 1)
        self.assertEqual(UserCollect.objects.get(user_id=user), user_collect)
        
        # Delete
        user_collect.delete()
        self.assertEqual(UserCollect.objects.count(), 0)
    
    def test_user_view_model(self):
        user = User.objects.get(openid='test_openid')
        product = Product.objects.get(id=1)
        user_view = UserView.objects.create(user_id=user, product_id=product, time=timezone.now())
        self.assertEqual(user_view.user_id, user)
        self.assertEqual(user_view.product_id, product)

        # Read
        self.assertEqual(UserView.objects.count(), 1)
        self.assertEqual(UserView.objects.get(user_id=user), user_view)
        
        # Delete
        user_view.delete()
        self.assertEqual(UserView.objects.count(), 0)
    
    def test_user_value_model(self):
        user = User.objects.get(openid='test_openid')
        product = Product.objects.get(id=1)
        user_value = UserValue.objects.create(user_id=user, product_id=product, value_or_not=1)
        self.assertEqual(user_value.user_id, user)
        self.assertEqual(user_value.product_id, product)
        self.assertEqual(user_value.value_or_not, 1)

        # Read
        self.assertEqual(UserValue.objects.count(), 1)
        self.assertEqual(UserValue.objects.get(user_id=user), user_value)
        
        # Update
        user_value.value_or_not = 0
        user_value.save()
        self.assertEqual(UserValue.objects.get(user_id=user).value_or_not, 0)
        
        # Delete
        user_value.delete()
        self.assertEqual(UserValue.objects.count(), 0)


# 测试接口全部函数
class ViewTestCase(TestCase):
    
    def setUp(self):
        self.client = Client()
        self.product1 = Product.objects.create(id=1, name="test_product_1", image="test_image_1", pics=["test_pics_1"], 
                               price=10, value=20, notvalue=30, referrer_id="test_openid_1", recommended_time=timezone.datetime(2023, 6, 1, 10, 30),
                               purchase_method='test_channel_1', recommendation_reason="test_reason_1",
                               recent_prices=[{'price':50, 'time':"test_recent_time"}], introduce="test_introduce_1")

        self.product2 = Product.objects.create(id=2, name="test_product_2", image="test_image_2", pics=["test_pics_2"], 
                               price=40, value=50, notvalue=60, referrer_id="test_openid_2", recommended_time=timezone.datetime(2023, 6, 2, 10, 30),
                               purchase_method='test_channel_2', recommendation_reason="test_reason_2",
                               recent_prices=[{'price':100, 'time':"test_recent_time_2"}], introduce="test_introduce_2")
        self.user = User.objects.create(openid='test_openid', nickName='Test_User', avatarUrl='test_avatar')
        self.comment = Comment.objects.create(user=self.user, good_id=self.product1, content='Test Comment', time=timezone.datetime(2023, 6, 4, 10, 30))

    
    def test_get_product(self):
        response = self.client.get(reverse('get_product'))
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        expected_data = {'products': serializer.data}
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
    
    def test_get_product_detail(self):
        response = self.client.get(reverse('get_product_detail', args=[self.product1.id]))
        products = Product.objects.filter(id=self.product1.id)
        serializer = ProductSerializer(products, many=True)
        expected_data = {'products': serializer.data}
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
    
    def test_get_product_new(self):
        response = self.client.get(reverse('get_product_new'))
        products = Product.objects.all().order_by('-recommended_time')
        serializer = ProductSerializer(products, many=True)
        expected_data = {'products': serializer.data}
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
    
    def test_get_product_hot(self):
        response = self.client.get(reverse('get_product_hot'))
        products = Product.objects.all().order_by('-value')
        serializer = ProductSerializer(products, many=True)
        expected_data = {'products': serializer.data}
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    
    # def test_get_front_product(self):
    #     response = self.client.get(reverse('get_front_product'))
    #     products = Product.objects.annotate(random_order=Random()).order_by('random_order')
    #     serializer = ProductSerializer(products, many=True)
    #     expected_data = {'products': serializer.data}
    #     # print(response.json())  # 输出实际结果
    #     # print(expected_data)    # 输出预期结果
    #     self.assertEqual(response.status_code, 200)
    #     self.assertDictEqual(response.json(), expected_data)
    
    def test_search_products(self):
        url = reverse('search_products')
        search_text = 'test'
        mode = 'all'
        
        response = self.client.get(url, {'str': search_text, 'mode': mode})
        products = Product.objects.filter(Q(name__icontains=search_text) | Q(image__icontains=search_text) |
                                          Q(pics__icontains=search_text) | Q(referrer_id__icontains=search_text) |
                                          Q(purchase_method__icontains=search_text) |
                                          Q(recommendation_reason__icontains=search_text) |
                                          Q(introduce__icontains=search_text))
        serializer = ProductSerializer(products, many=True)
        expected_data = {'products': serializer.data}
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)
    
    def test_add_collect(self):
        url = reverse('add_collect')
        good_id = self.product1.id
        openid = self.user.openid
        
        response = self.client.get(url, {'good_id': good_id, 'openid': openid})
        user_collect = UserCollect.objects.filter(user_id=self.user, product_id=self.product1).exists()
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(user_collect)

    def test_delete_collect(self):
        url = reverse('delete_collect')
        good_id = self.product1.id
        openid = self.user.openid
        
        response = self.client.get(url, {'good_id': good_id, 'openid': openid})
        user_collect = UserCollect.objects.filter(user_id=self.user, product_id=self.product1).exists()
        
        self.assertEqual(response.status_code, 200)
        self.assertFalse(user_collect)
    
    def test_get_product_pic(self):
        url = reverse('get_product_pic')
        good_id = self.product1.id
        
        response = self.client.get(url, {'good_id': good_id})
        product = Product.objects.get(id=good_id)
        expected_data = {'image_urls': [product.image] + product.pics}  # 修改预期结果
        
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), expected_data)

    
    def test_get_user_comment(self):
        url = reverse('get_user_comment')
        openid = self.user.openid
        
        response = self.client.get(url, {'openid': openid})
        comments = Comment.objects.filter(user=self.user)
        comment_list = [
            {
                'content': comment.content,
                'time': comment.time.isoformat() + '+00:00',
                'product_id': comment.good_id.id
            }
            for comment in comments
        ]
        expected_data = {'comments': comment_list}
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        # Extract content and product_id fields from response_data
        response_comments = [{'content': comment['content'], 'product_id': comment['product_id']} for comment in response_data['comments']]

        # Extract content and product_id fields from expected_data
        expected_comments = [{'content': comment['content'], 'product_id': comment['product_id']} for comment in expected_data['comments']]

        self.assertEqual(response_comments, expected_comments)
    
    def test_add_comment(self):
        url = reverse('add_comment')
        openid = self.user.openid
        good_id = self.product1.id
        content = 'New Comment'
        
        response = self.client.get(url, {'openid': openid, 'good_id': good_id, 'commentStr': content})
        comment = Comment.objects.filter(user=self.user, good_id=self.product1, content=content).exists()
        
        self.assertEqual(response.status_code, 200)
        self.assertTrue(comment)
    
    def test_get_product_comment(self):
        url = reverse('get_product_comment')
        good_id = self.product1.id
        
        response = self.client.get(url, {'good_id': good_id})
        comments = Comment.objects.filter(good_id=self.product1)
        comment_list = [{'content': comment.content, 'time': comment.time.isoformat(), 'user': comment.user.openid} for comment in comments]
        expected_data = {'comment': comment_list}
        
        self.assertEqual(response.status_code, 200)
        response_data = response.json()

        # Extract user and content fields from response_data
        response_comments = [{'user': comment['user'], 'content': comment['content']} for comment in response_data['comment']]

        # Extract user and content fields from expected_data
        expected_comments = [{'user': comment['user'], 'content': comment['content']} for comment in expected_data['comment']]

        self.assertEqual(response_comments, expected_comments)

    def test_add_product(self):
        url = reverse('add_product')
        params = {
            'name': 'Test Product',
            'price': '9.99',
            'description': 'Test Description',
            'purchaseChannel': 'Online',
            'recommendationReason': 'Test Reason',
            'imageUrl_1': 'image1.jpg',
            'imageUrl_2': 'image2.jpg',
            'imageUrl_3': 'image3.jpg',
            'imageUrl_4': 'image4.jpg',
            'userId': 'test_user',
            'prices': '[{"Date": "2023-01-01", "Price": "9.99"}]'
        }

        response = self.client.get(url, params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), '上传成功')

    def test_delete_product(self):
        url = reverse('delete_product')
        params = {
            'name': 'Test Product'
        }

        response = self.client.get(url, params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'删除成功': True})

    def test_delete_manage_comment(self):
        url = reverse('delete_manage_comment')
        params = {
            'openid': 'test_openid',
            'product_id': '1',
            'content': 'Test Comment'
        }

        response = self.client.get(url, params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'删除成功': True})

    def test_get_user_collect(self):
        url = reverse('get_user_collect', args=['test_openid'])

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('products', response.json())
        self.assertIsInstance(response.json()['products'], list)

    def test_create_user(self):
        url = reverse('create_user')
        params = {
            'openid': 'test_user',
            'nickName': 'Test User',
            'avatarUrl': 'avatar.jpg'
        }

        response = self.client.get(url, params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'注册成功': True})

    def test_get_user(self):
        url = reverse('get_user')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.assertIn('users', response.json())
        self.assertIsInstance(response.json()['users'], list)

    def test_delete_user(self):
        url = reverse('delete_user')
        params = {
            'openid': 'test_user'
        }

        response = self.client.get(url, params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'删除成功': True})


    def test_value_or_not(self):
        url = reverse('value_or_not')
        data = {
            'userId': self.user.openid,
            'goodInfo': self.product1.name,
            'value': 1
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {'message': '评价已添加'})

    def test_get_user_value(self):
        url = reverse('get_user_value')
        data = {
            'openid': self.user.openid
        }
        response = self.client.get(url, data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['user_values'], [])
    
    def tearDown(self):
        User.objects.all().delete()
        Product.objects.all().delete()
        Comment.objects.all().delete()