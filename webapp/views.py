from django.shortcuts import render
from django.views import generic
from .models import Blogs, Comments, Users

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'index.html'


    def get_queryset(self):
        return Users.objects.all()