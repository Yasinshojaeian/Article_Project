from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
# Create your views here.

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username, password=password)
        if user is not None :
            login(request,user)
            return redirect('/')
        else :
            return HttpResponse('your not login ')
    return render (request, 'auth/index.html')

def user_logout(request):
    logout(request)
    return redirect('/')

