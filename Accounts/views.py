from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from ReadBook.models import UserInfo
# Create your views here.

def register_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            user_type = request.POST['user_type']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, "Username is already taken")
                    return redirect ("Accounts/register_user")
                
                elif User.objects.filter(email=email).exists():
                    messages.info(request, "Email is already taken")
                    return redirect ("Accounts/register_user")

                else:
                    user = User.objects.create_user(username=username,password=password1,
                    email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    UserInfo.objects.create(id=user.id,user_type=user_type,users_id=user.id)
                    messages.success(request,"Registration succeed !")
                    return redirect('/login')    
            else:
                messages.info(request,"Password did not match")
                return redirect ('Accounts/register_user')
        return render (request,"Accounts/register.html")
    else:
        return redirect('/')

def login_user(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']

            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,"Login success")
                return redirect('/')
            else:
                messages.success(request, "Wrong Credentials")
                return redirect('Accounts/login_user')
        else:
             return render(request,'Accounts/login.html')
    else:
        return redirect("/")

def logout_user(request):
    logout(request)
    messages.success(request,'Successfully logged out ! ')
    return redirect('login_user')
        