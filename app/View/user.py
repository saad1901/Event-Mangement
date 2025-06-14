from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime

@login_required
def user_profile(request):
    context = {
        'current_year': datetime.now().year
    }
    return render(request, 'user/profile.html', context)

@login_required
def edit_profile(request):
    if request.method == 'POST':
        # Handle profile update logic here
        messages.success(request, 'Profile updated successfully!')
        return redirect('user_profile')
    
    context = {
        'current_year': datetime.now().year
    }
    return render(request, 'user/edit_profile.html', context)

@login_required
def user_bookings(request):
    context = {
        'current_year': datetime.now().year
    }
    return render(request, 'user/bookings.html', context)

@login_required
def booking_detail(request, booking_id):
    context = {
        'current_year': datetime.now().year,
        'booking_id': booking_id
    }
    return render(request, 'user/booking_detail.html', context) 