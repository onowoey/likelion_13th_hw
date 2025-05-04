from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=10)
    content = models.TextField()
    date = models.DateTimeField()
    update_date = models.DateTimeField()
    image = models.ImageField(upload_to="blog/", blank=True, null=True)
    
    def __str__(self):
        return self.title #관리자(admin) 페이지나 셸 등에서 Post 객체를 문자열로 표현할 때 title 필드를 대표값처럼 보여주겠다
    
    def summary(self):
        return self.content[:20]