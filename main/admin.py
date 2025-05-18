from django.contrib import admin
from .models import * #현재 앱의 models.py 에서 모든것을 가져옴
# Register your models here.
admin.site.register(Post) #Post 를 admin에서 볼수 있게 해줌
admin.site.register(Comment)
admin.site.register(Tag)
