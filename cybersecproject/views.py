from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators import csrf
from django.views.decorators.csrf import csrf_exempt

from cybersecproject.models import HomePage

def login(request):
    error = None
    if request.method == "POST":
        user = auth.authenticate(request, username = request.POST.get("username"), password = request.POST.get("password"))
        if user is not None:
            auth.login(request, user)
            return redirect("homepage", request.user.username)
        else:
            error = "Invalid credentials"
    return render(request, "login.html", {"error": error})

@login_required
@csrf_exempt
def homepage(request, username):
    if request.method == "POST":
        homepage = HomePage.objects.get(user=request.user)
        homepage.welcome_message = request.POST.get("welcome_message")
        homepage.save()
        return redirect("homepage", request.user.username)
    else:
        homepage_owner = User.objects.get(username=username) if username != "" else request.user
        homepage, created = HomePage.objects.get_or_create(
            user = homepage_owner
        )
        if created:
            homepage.welcome_message = "Welcome to my homepage!"
            homepage.save()
        users = User.objects.all()
        return render(request, "home.html", {"user": request.user, "users": users, "homepage": homepage})

@login_required
def index(request):
    return redirect("homepage", request.user)