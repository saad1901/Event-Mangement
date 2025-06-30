from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is None:
            messages.error(request, 'Invalid ID or Passaword')
            return redirect('login')

        login(request, user)
        messages.success(request, 'Login Successful')
        return redirect('admin_dashboard')

    if request.user.is_authenticated:
        return redirect('admin_dashboard')
    else:
        return render(request, 'login/login.html')

def logout_view(request):
    logout(request)
    # messages.success(request, 'You have been logged out successfully!')
    return redirect('login')

def register(request):
    if request.method == 'POST':
        # Handle registration logic here
        pass
    return render(request, 'auth/register.html') 