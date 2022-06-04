from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.urls import reverse


def home(request):
    return render(request, "polls/home.html")


def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        password = request.POST["password"]
        password1 = request.POST["password1"]

        if password == password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, "email already used")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "username already taken")
                return redirect('signup')
            else:
                myuser = User.objects.create_user(username, email, password)
                myuser.first_name = fname
                myuser.last_name = lname
                myuser.save()
                messages.success(request, "account created successfully")
                return redirect('signin')
        else:
            messages.info(request, "password do not march")
            return redirect('signup')
    else:
        return render(request, "polls/signup.html")


def signin(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, "polls/mian.html")
        else:
            messages.error(request, "create an account to login")
            return redirect("signup")
    else:
        return render(request, "polls/signin.html")


def signout(request):
    logout(request)
    return render(request, "polls/home.html")
