from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE , verbose_name='کاربر')
    full_name = models.CharField(max_length=60 , verbose_name='نام')
    family = models.CharField(max_length=100 , verbose_name='نام خاتوادگی ')
    profile = models.ImageField(upload_to ='images/user',verbose_name='پروفایل ')
    
    
    