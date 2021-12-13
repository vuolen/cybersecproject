from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login(request):
    error = None
    if request.method == "POST":
        user = authenticate(request, username = request.POST.get("username"), password = request.POST.get("password"))
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            error = "Invalid credentials"
    return render(request, "login.html", {"error": error})