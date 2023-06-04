from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from app.models import User, Product, Comment, UserCollect, UserView, UserValue
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
