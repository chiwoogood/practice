from django.shortcuts import render, redirect
from .models import Post
# Create your views here.

def index(request):
    
    # 1. 모든 글 목록을 보여준다
    # 2. template에 보내준다
    posts = Post.objects.all()
    context = {
        'posts' : posts
    }
    return render(request,'posts/index.html',context)


def new(request):
    return render(request,'posts/new.html')

def create(request):
    
    # 1. parameter로 날라온 데이터를 DB에 저장
    title = request.GET.get('title')
    content = request.GET.get('content')
    context = {
        'title' :title,
        'content' : content,
    }
    # 2.DB에 저장
    Post.objects.create(title=title, content=content)
    return render(request,'posts/create.html',context)

def delete(request,pk):
    Post.objects.get(id=pk).delete()
    return redirect('posts:index')
    