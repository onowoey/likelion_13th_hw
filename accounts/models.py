from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    nickname = models.CharField(max_length=10)
    grade = models.CharField(max_length=10, default='1')
    school = models.TextField(null=True)
    