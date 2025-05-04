from django.shortcuts import render, redirect , get_object_or_404
from django.utils import timezone
from .models import *

# Create your views here.
def mainpage(request):
    context = {
        "generation": 2,
        "info": {'variable': '변수', 'tag': '태그', 'filter': '필터'},
    }
    return render(request, 'main/mainpage.html', context)

def secondpage(request):
    posts = Post.objects.all()
    return render(request, 'main/secondpage.html',{'posts': posts})#오른쪽 posts(DB 필드명)에서 왼쪽 posts 이름으로 넘겨줌

def new_post(request):
    return render(request, 'main/new-post.html')#사용자가 글을 새로 쓰기 위해 들어왔을 때 보여주는 화면.

def detail(request,id):
    post = get_object_or_404(Post, pk= id)
    return render(request, 'main/detail.html', {'post':post})

def edit(request, id):
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {"post": edit_post})

def create(request):
    new_post = Post()
    
    new_post.title = request.POST['title']
    new_post.author = request.POST['author']
    new_post.content = request.POST['content']
    new_post.date = timezone.now()
    new_post.update_date = timezone.now()
    new_post.image = request.FILES.get('image')
    
    new_post.save()
    
    return redirect('main:detail', new_post.id)

def update(request,id):
    update_post = Post.objects.get(pk=id)
    update_post.title = request.POST['title']
    update_post.author = request.POST['author']
    update_post.content = request.POST['content']
    update_post.update_date = timezone.now()
    update_post.image = request.FILES.get('image')
    
    update_post.save()
    return redirect('main:detail', update_post.id)

def delete(request,id):
    delete_post = Post.objects.get(pk=id)
    delete_post.delete()
    
    return redirect('main:secondpage')