from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from Users.models import profile
from django.contrib.auth.models import User
from django.contrib import messages


def home(request):
    return render(request, "landing.html")

def login_page(request):
    if request.method=='POST':
        loginusername=request.POST['loginusername']
        loginpassword=request.POST['loginpassword']
        user=authenticate(request, username=loginusername, password=loginpassword)
        if user is not None:
            login(request, user)
            # messages.success(request, "success")
            return redirect('home')
        else:
            
            messages.error(request, "error")
            
    return render(request, "login.html")