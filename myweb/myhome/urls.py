from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.index,name="index"),
    # 定义路由 显示页面
    url(r'^citys/$',views.citys,name="citys"),
    # 定义路由 用于获取城市信息
    url(r'^getcitys/$',views.getcitys,name="getcitys"),
    
]
