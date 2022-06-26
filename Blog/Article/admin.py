from django.contrib import admin

from Article.models import Article , Category , IpAddress , Comment

# Register your models here.
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(IpAddress)
admin.site.register(Comment)