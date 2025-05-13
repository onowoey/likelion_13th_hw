from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from main.models import *
from accounts.models import *

# Create your views here.
def mypage(request, id):
    user = get_object_or_404(User, pk = id)
    profile, created = Profile.objects.get_or_create(user=user)
    postlist = Post.objects.filter(author= profile.nickname) 
    context = {
        'user': user,
        'postlist':postlist
    }
    return render(request, 'users/mypage.html', context)