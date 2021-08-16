from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Blog
# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog(request):
    blog_objects = Blog.objects.all()
    all_blog_list = []
    for item in blog_objects:
        all_blog_list.append(item)
    print(blog_objects)
    context = {
        "blogs" : all_blog_list
    }
    return render(request, 'blog.html', context)

def invest(request):
    return render(request, 'invest.html')

def contact(request):
    return render(request, 'contact.html')