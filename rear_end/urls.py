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
from app import manage
from app import tips_commit
from app import focus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', views.create),
    path('api/product', views.get_product, name='get_product'),
    path('api/product_new', views.get_product_new, name='get_product_new'),
    path('api/product_hot', views.get_product_hot, name='get_product_hot'),
    path('api/user_collect/<int:user_id>/', views.get_user_collect, name='get_user_collect'),
    path('api/user_value/<int:user_id>/<int:value_flag>', views.get_user_value, name='get_user_value'),
    path('api/user_new_break/<int:user_id>', views.get_user_new_break, name='get_user_new_break'),
    path('api/user_hot_break/<int:user_id>', views.get_user_hot_break, name='get_user_hot_break'),
    path('api/user_make_comment/<int:user_id>', views.get_make_comment, name='get_make_comment'),
    path('api/user_get_comment/<int:user_id>', views.get_comment, name='get_comment'),
    path('api/manager_get', manage.manager_get, name='manager_get'),
    path('api/user_submit_break', tips_commit.submit_break, name='submit_break'),
    path('api/user_get_goodsList/<int:user_id>', focus.getgoodsList1, name='getgoodsList1'),

]
