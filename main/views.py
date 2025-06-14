from django.shortcuts import render, redirect , get_object_or_404
from django.utils import timezone
from .models import *
import re

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
    if request.method =='GET':
        comments = Comment.objects.filter(post=post)
        return render(request, 'main/detail.html', {'post':post, 'comments':comments})
    elif request.method == 'POST':
        new_comment = Comment()
        new_comment.post = post
        new_comment.author=request.user
        new_comment.content = request.POST['content']
        new_comment.date = timezone.now()
        new_comment.save()
        return redirect('main:detail', id)
    
def likes(request, post_id):
    post = get_object_or_404(Post, id = post_id)
    if request.user in post.like.all():
        post.like.remove(request.user)
        post.like_count -= 1
        post.save()
    else:
        post.like.add(request.user)
        post.like_count += 1
        post.save()
        
    return redirect('main:detail', post.id)
        

def edit(request, id):##수정중
    edit_post = Post.objects.get(pk=id)
    return render(request, 'main/edit.html', {"post": edit_post})

def create(request):
    if request.user.is_authenticated:
        
        new_post = Post()
        
        new_post.title = request.POST['title']
        new_post.author = request.user
        new_post.content = request.POST['content']
        new_post.date = timezone.now()
        new_post.update_date = timezone.now()
        new_post.image = request.FILES.get('image')
        
        new_post.save()
        
        words = re.split(r'[\s]+', new_post.content.strip())
        tag_list = []
        
        for w in words:
            if len(w)>0:
                if w[0] =='#':
                    tag_list.append(w[1:])
        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            new_post.tags.add(tag)
            
        return redirect('main:detail', new_post.id)
    else:
        return redirect('accounts:login')

def update(request,id):##수정된 걸 업데이트
    update_post = Post.objects.get(pk=id)
    if request.user.is_authenticated and request.user == update_post.author:
        update_post.title = request.POST['title']
        update_post.content = request.POST['content']
        update_post.update_date = timezone.now()
        
        update_post.tags.clear()
        
        words = re.split(r'[\s]+', update_post.content.strip())
        tag_list = []
        
        for w in words:
            if len(w)>0:
                if w[0] =='#':
                    tag_list.append(w[1:])
        for t in tag_list:
            tag, boolean = Tag.objects.get_or_create(name=t)
            update_post.tags.add(tag)
        
        if request.FILES.get('image'):
            update_post.image = request.FILES.get('image')
        update_post.save()
        
        return redirect('main:detail', update_post.id)
    return redirect('accounts:login', update_post.id)

def delete(request,id):
    delete_post = Post.objects.get(pk=id)
    if request.user.is_authenticated and request.user == delete_post.author:
        delete_post.delete()
    
    return redirect('main:secondpage')

def comment_delete(request,post_id,comment_id):
    comments = Comment.objects.get(pk = comment_id)
    if request.user.is_authenticated and request.user == comments.author:
        comments.delete()
        
    return redirect('main:detail', post_id)

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'main/tag-list.html', {'tags':tags})

def tag_post(request, tag_id):
    tag = get_object_or_404(Tag, id = tag_id)
    posts = tag.posts.all()
    return render(request, 'main/tag-post.html',{
        'tag':tag,
        'posts':posts
    })