from django.db import models

# Create your models here.

# 创建blogs表
class Blogs(models.Model):
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_image = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    content = models.TextField(verbose_name=None)
    created_at = models.DateTimeField(verbose_name=None)


# 创建comments表
class Comments(models.Model):
    blog_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50)
    user_image = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    content = models.TextField(verbose_name=None)
    created_at = models.DateTimeField(verbose_name=None)


# 创建users表
class Users(models.Model):
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    admin = models.IntegerField(max_length=20)
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    created_at = models.DateTimeField(verbose_name=None)
