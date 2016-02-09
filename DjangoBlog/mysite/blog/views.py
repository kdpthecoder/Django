from django.shortcuts import render
from blog.models import Post
from blog.models import Comment

# Create your views here.

def view_posts(request):
    posts = Post.objects.all().order_by("create_time");
    return render(request, 'posts.html', {'posts': posts});


def view_post(request, pk):
    p = Post.objects.get(pk=pk);
    c = Comment.objects.filter(post=p)
    return render(request,'post.html',{'post' : p, 'comments': c});


def view_home(request):
    pass	



