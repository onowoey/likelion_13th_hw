from django.db import models
from django.contrib.auth.models import User
from .models import *

# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, null= False, blank=False, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateTimeField()
    update_date = models.DateTimeField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    tags = models.ManyToManyField(Tag, related_name= 'posts', blank=True)
    
    def __str__(self):
        return self.title #관리자(admin) 페이지나 셸 등에서 Post 객체를 문자열로 표현할 때 title 필드를 대표값처럼 보여주겠다
    
    def summary(self):
        return self.content[:20]
    
class Comment(models.Model):
    content = models.TextField()
    date = models.DateTimeField()
    author = models.ForeignKey(User, null=False, blank = False, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, null=False, blank = False, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.post.title + ":" + self.content[:20]+ "by" + self.author.profile.nickname