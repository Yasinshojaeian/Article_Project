from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from account.models import Profile
# Create your views here.

def user_login(request):
    if request.user.is_authenticated :
        return redirect('/')
    if request.method == 'POST':
        username = request.POST.get('username')
        print (username)
        password = request.POST.get('password')
        print(password)
        user = authenticate(request,username=username, password=password)
        if user is not None :
            login(request,user)
            return redirect('/')
    return render (request, 'auth/index.html')

def user_logout(request):
    logout(request)
    return redirect('/')


def user_register(request):
    if request.method == 'POST':
        context = {'errors':[]}
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        if password != password2 :
            context['errors'].append('Password is same')
            return render(request, 'auth/register.html',context)
        if User.objects.filter(username=username):
            context['errors'].append('Username already exist')
            return render(request, 'auth/register.html',context)

        user = User.objects.create(username=username, email=email, password=password)
        login(request,user)
        return redirect('/')
    return render(request, 'auth/register.html')
