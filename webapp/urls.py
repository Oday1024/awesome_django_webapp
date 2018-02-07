#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 09:49
# @Author  : ShenFeng
# @Site    : 
# @File    : urls.py
# @Software: PyCharm


from django.urls import path
from . import views


app_name = 'webapp'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
]