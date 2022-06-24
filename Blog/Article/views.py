from django.shortcuts import render
from Article.models import Article

# Create your views here.

def detail_view(request,pk=None):
    article = Article.objects.filter(id=pk).first()
    return render(request,'home/post-details.html',context={'article':article})