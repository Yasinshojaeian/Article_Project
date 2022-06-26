from re import T
from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name='نام')
    
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'دسته بندی '
        verbose_name_plural = 'دسته بندی '
        
        
        
class IpAddress(models.Model):
    ip_address = models.GenericIPAddressField(verbose_name='آدرس آی پی ')
class Article(models.Model):
    STATUS_CHOICES = (
        ('p','منتشر شده'),
        ('d','پیش نویس'),
    )
    name = models.CharField(max_length=100,verbose_name='نام')
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name='دسته بندی')
    image = models.ImageField(upload_to='images/article',verbose_name='تصویر')
    author = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='نویسنده')
    create_date = models.DateField(auto_now_add=True,verbose_name='تاریخ ایجاد')
    body = models.TextField(verbose_name='توضیحات')
    status = models.CharField(max_length=1, choices=sorted(STATUS_CHOICES),verbose_name='وضعیت',default='d')
    hits = models.ManyToManyField(IpAddress,verbose_name='آدرس آی پی ')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name ='مقاله'
        verbose_name_plural = 'مقالات'

class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete=models.CASCADE,related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE , related_name='comments')
    parent = models.ForeignKey('self',on_delete=models.CASCADE,related_name='replise',null=True , blank=True)
    body = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body[:50]
    
    
    