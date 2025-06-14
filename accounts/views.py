from django.shortcuts import render, redirect , get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(request, username= username, password= password)
        
        if user is not None:
            auth.login(request,user)
            return redirect('main:mainpage')
        else:
            return render(request, 'accounts/login.html')
        
    elif request.method == 'GET':
        return render(request, 'accounts/login.html')
    
def logout(request):
    auth.logout(request)
    return redirect('main:mainpage')

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['confirm']:
            user = User.objects.create_user(
                username = request.POST['username'],
                password = request.POST['password']
            )
            #nickname = request.POST['nickname']
            #grade = int(request.POST['grade'])
            #school = request.POST['school']
            
            #profile = Profile(user= user, nickname = nickname, grade = grade, school= school)
            #profile.save()
            
            auth.login(request, user)
            return redirect('/')
    return render(request, 'accounts/signup.html')
