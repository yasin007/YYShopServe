"""YYShopServe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.contrib import admin
from django.conf.urls import url, include
from rest_framework_jwt.views import obtain_jwt_token
from rest_framework.routers import DefaultRouter
from users.views import SmsCodeViewset, UserViewset
import xadmin

router = DefaultRouter()
# 发送验证码
router.register(r'codes', SmsCodeViewset, base_name="codes")
# 注册
router.register(r'users', UserViewset, base_name="users")

urlpatterns = [

    url(r'^', include(router.urls)),
    # 后台管理平台
    url(r'^xadmin/', xadmin.site.urls),
    # jwt的认证接口
    # url(r'^login/', obtain_jwt_token),
]
