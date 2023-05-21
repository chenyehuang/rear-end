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
    path('api/user_collect/<int:user_id>/', views.get_user_collect, name='get_user_collect'),
    path('api/user_value/<int:user_id>/<int:value_flag>', views.get_user_value, name='get_user_value'),
    path('api/user_new_break/<int:user_id>', views.get_user_new_break, name='get_user_new_break'),
    path('api/user_hot_break/<int:user_id>', views.get_user_hot_break, name='get_user_hot_break'),
    path('api/user_make_comment/<int:user_id>', views.get_make_comment, name='get_make_comment'),
    path('api/user_get_comment/<int:user_id>', views.get_comment, name='get_comment'),
    path('api/user_hot_break/<int:user_id>', views.history_hot_product, name='history_hot_product'),
    path('api/user_new_break/<int:user_id>', views.history_new_product, name='history_new_product'),

]
