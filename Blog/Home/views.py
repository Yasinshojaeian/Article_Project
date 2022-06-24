from django.shortcuts import render
from Article.models import Article

# Create your views here.

def home(request):
    articles = Article.objects.filter(status = 'p')
    return render (request, 'home/index.html',context={'articles':articles})