from django.db import models

# Create your models here.


# 创建users表
class Users(models.Model):
    email = models.CharField(max_length=50)
    passwd = models.CharField(max_length=50)
    admin = models.IntegerField()
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=500)
    created_at = models.DateTimeField(verbose_name=None)


# 创建blogs表
class Blogs(models.Model):
    # on_delete=models.CASCADE，表示当user被删除时，删除对应user的blog表记录
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    user_image = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    content = models.TextField(verbose_name=None)
    created_at = models.DateTimeField(verbose_name=None)


# 创建comments表
class Comments(models.Model):
    # on_delete=models.CASCADE，表示当user被删除时，删除对应user的comments表记录
    # on_delete=models.CASCADE，表示当blog_id被删除时，删除对应blog的comments表记录
    blog_id = models.ForeignKey(Blogs, on_delete=models.CASCADE)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE)
    user_name = models.CharField(max_length=50)
    user_image = models.CharField(max_length=500)
    name = models.CharField(max_length=50)
    summary = models.CharField(max_length=200)
    content = models.TextField(verbose_name=None)
    created_at = models.DateTimeField(verbose_name=None)