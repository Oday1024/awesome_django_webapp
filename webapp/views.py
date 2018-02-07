from django.shortcuts import render
from django.views import generic
from .models import Users, Blogs, Comments

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'blog_list'

    # 返回日志列表所有内容
    def get_queryset(self):
        return Blogs.objects.all()