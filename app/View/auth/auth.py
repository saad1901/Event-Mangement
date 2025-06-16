from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        # Handle login logic here
        pass
    return render(request, 'auth/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been logged out successfully!')
    return redirect('home')

def register(request):
    if request.method == 'POST':
        # Handle registration logic here
        pass
    return render(request, 'auth/register.html') 