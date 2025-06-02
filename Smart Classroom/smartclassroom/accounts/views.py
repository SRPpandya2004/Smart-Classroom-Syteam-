from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def registration(request):
    return render(request, "registration.html")

def signin(request):
    return render(request, "signin.html")