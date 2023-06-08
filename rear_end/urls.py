"""
URL configuration for rear_end project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create),
    path('api/product', views.get_product, name='get_product'),
    path('api/user', views.get_user, name='get_user'),
    path('api/product/<int:product_id>', views.get_product_detail, name='get_product_detail'),
    path('api/product_new', views.get_product_new, name='get_product_new'),
    path('api/product_hot', views.get_product_hot, name='get_product_hot'),
    path('api/create_user/', views.create_user, name="create_user"),
    path('api/front_product/', views.get_front_product, name='get_front_product'),
    path('api/search_products', views.search_products, name='search_products'),
    path('api/add_collect', views.add_collect, name='add_collect'),
    path('api/delete_collect', views.delete_collect, name='delete_collect'),
    path('api/get_product_pic/', views.get_product_pic, name='get_product_pic'),
    path('api/get_user_comment/', views.get_user_comment, name='get_user_comment'),
    path('api/add_comment/', views.add_comment, name='add_comment'),
    path('api/user_collect/<openid>/', views.get_user_collect, name='get_user_collect'),
    path('api/get_product_comment/', views.get_product_comment, name='get_product_comment'),
    path('api/add_product/', views.add_product, name='add_product'),
    path("api/delete_user/",views.delete_user, name='delete_user'),
    path("api/delete_product/",views.delete_product, name='delete_product'),
    path('api/delete_manage_comment/', views.delete_manage_comment, name='delete_manage_comment'),
    path('api/value_or_not/', views.value_or_not, name='value_or_not'),
    path('api/get_user_value/', views.get_user_value, name='get_user_value'),
    path('api/opinion/', views.opinion, name='opinion'),
    path('api/get_break/', views.get_break, name='get_break'),
    path('api/get_all_comment/', views.get_all_comment, name='get_all_comment'),
]
