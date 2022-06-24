from django.shortcuts import render
from Article.models import Article
from account.models import Profile

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        profile = Profile.objects.filter(user=request.user).first()
        articles = Article.objects.filter(status = 'p')
        return render (request, 'home/index.html',context={'articles':articles,'profile':profile})
    else :
        articles = Article.objects.filter(status = 'p')
        return render (request, 'home/index.html',context={'articles':articles})