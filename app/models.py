from django.db import models


# Create your models here.
# class User(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     user_name = models.CharField(max_length=200)
#     user_wechat = models.CharField(max_length=200)
#     phone_number = models.BigIntegerField()

class User(models.Model):
    openid = models.CharField(max_length=200)
    nickName = models.CharField(max_length=200)
    avatarUrl = models.CharField(max_length=200)

# class User_new(models.Model):
#     openid = models.CharField(max_length=200)
#     nickName = models.CharField(max_length=200)
#     avatarUrl = models.CharField(max_length=200)

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    pics = models.JSONField()
    price = models.FloatField()
    value = models.IntegerField()
    notvalue = models.IntegerField()
    referrer_id = models.CharField(max_length=200)
    recommended_time = models.DateTimeField()
    purchase_method = models.CharField(max_length=200)
    recommendation_reason = models.CharField(max_length=200)
    recent_prices = models.JSONField()
    introduce = models.TextField()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    good_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)


class UserCollect(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)

    # 防止出现相同的行
    class Meta:
        unique_together = ['user_id', 'product_id']


class UserView(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    time = models.DateTimeField()

    class Meta:
        unique_together = ['user_id', 'product_id']


class UserValue(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    VALUE_OR_NOT_CHOICES = (
        (0, 'Not Value'),
        (1, 'Value'),
    )
    value_or_not = models.IntegerField(choices=VALUE_OR_NOT_CHOICES)

    class Meta:
        unique_together = ['user_id', 'product_id']
