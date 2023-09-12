from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 
from django.contrib import messages
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
@login_required(login_url='login')
def home(request):
    return render (request,'home.html')

@never_cache
def signup_page(request):
    return render (request,'signup_page.html')

@never_cache
def login_page(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=username,password=password)
        print(user)
        if user is not None:
           login(request,user)
           return redirect('home')
        else:
            messages.error(request,"Invalid Username or Password")
            return redirect ('login')

    return render(request,'login_page.html')

@never_cache
def signin_page(request):
    if request.method=="POST":
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password')
        confirm_password=request.POST.get('confirm-password')

        if not username or not email or not password:
            messages.error(request,'please fill all the field')
            return redirect('signin')

        if User.objects.filter(username=username).exists():
            messages.error (request,'user already exist')
            return redirect('signin')

        if password==confirm_password:
            User.objects.create_user(username=username,password=password,email=email)
            return redirect('login')
        else:
            messages.error(request,"password mismatch")
            return redirect('signin')
    return render(request,'signin.html')        

@never_cache
def logout_page(request):
    logout(request)
    return redirect('login')



