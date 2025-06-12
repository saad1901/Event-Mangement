from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import *

def addparticipant(request):
    print(111)
    if request.method == 'POST':

        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        tickets = request.POST.get('tickets', 1)
        event_id = request.POST.get('event_id')
        if 'payment_screenshot' in request.FILES:
            screenshot = request.FILES['payment_screenshot']
        registration_id = datetime.now().strftime("%Y%m%d%H%M%S")
        
        # Create registration data (in a real app, this would be saved to the database)
        registration_data = {
            'id': registration_id,
            'name': name,
            'email': email,
            'phone': phone,
            'tickets': tickets,
            'event_id': event_id,
            'registration_date': datetime.now().strftime("%B %d, %Y %H:%M:%S")
        }
        
        # Set submitted flag to show success message
        submitted = True
        
        # In a real application, you would send confirmation emails/SMS here

        # Check if this is an AJAX request
        is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
        if is_ajax:
            # Return JSON response for AJAX requests
            return JsonResponse({
                'success': True,
                'message': 'Registration successful',
                'registration': registration_data
            })
            
        # Redirect to avoid form resubmission on refresh
        # Store registration data in session for retrieval after redirect
        request.session['registration_success'] = True
        request.session['registration_data'] = registration_data
        return redirect('event_detail_success', event_id=event_id)