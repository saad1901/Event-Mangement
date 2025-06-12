from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import *
# Create your views here.
def home(request):
    # Dummy events data
    current_date = datetime.now()
    
    events = [
        {
            'id': 1,
            'title': 'Tech Conference 2023',
            'description': 'Join industry leaders for a day of innovation and networking in the tech world.',
            'date': (current_date + timedelta(days=5)).strftime('%B %d, %Y'),
            'time': '9:00 AM',
            'location': 'Convention Center, New York',
            'image': 'static/images/tech-conference.jpg',
            'price': '$199.00',
            'category': 'Technology',
            'tickets_available': 500,
            'organizer': 'Tech Events Inc.'
        },
        # {
        #     'id': 2,
        #     'title': 'Summer Sports Festival',
        #     'description': 'Annual sports festival featuring various competitions and activities for all ages.',
        #     'date': (current_date + timedelta(days=7)).strftime('%B %d, %Y'),
        #     'time': '8:00 AM',
        #     'location': 'Central Park Stadium',
        #     'image': 'static/images/sports-festival.jpg',
        #     'price': '$45.00',
        #     'category': 'Sports',
        #     'tickets_available': 1000,
        #     'organizer': 'Sports Association'
        # },
        # {
        #     'id': 3,
        #     'title': 'Music Festival 2023',
        #     'description': 'Three days of amazing music performances from top artists around the world.',
        #     'date': (current_date + timedelta(days=15)).strftime('%B %d, %Y'),
        #     'time': '2:00 PM',
        #     'location': 'Riverside Park',
        #     'image': 'static/images/music-festival.jpg',
        #     'price': '$299.00',
        #     'category': 'Music',
        #     'tickets_available': 2000,
        #     'organizer': 'Music Events Co.'
        # },
        # {
        #     'id': 4,
        #     'title': 'Business Summit',
        #     'description': 'Network with industry leaders and learn about the latest business trends.',
        #     'date': (current_date + timedelta(days=20)).strftime('%B %d, %Y'),
        #     'time': '10:00 AM',
        #     'location': 'Grand Hotel, Chicago',
        #     'image': 'static/images/business-summit.jpg',
        #     'price': '$349.00',
        #     'category': 'Business',
        #     'tickets_available': 300,
        #     'organizer': 'Business Network'
        # },
        # {
        #     'id': 5,
        #     'title': 'Food & Wine Expo',
        #     'description': 'Experience the finest culinary delights and premium wines from around the world.',
        #     'date': (current_date + timedelta(days=25)).strftime('%B %d, %Y'),
        #     'time': '11:00 AM',
        #     'location': 'Exhibition Center',
        #     'image': 'static/images/food-expo.jpg',
        #     'price': '$89.00',
        #     'category': 'Food & Drink',
        #     'tickets_available': 800,
        #     'organizer': 'Gourmet Events'
        # },
        # {
        #     'id': 6,
        #     'title': 'Art & Design Expo',
        #     'description': 'Explore creative expressions from talented artists and designers showcasing their innovative work.',
        #     'date': (current_date + timedelta(days=10)).strftime('%B %d, %Y'),
        #     'time': '11:00 AM',
        #     'location': 'Metropolitan Gallery, Los Angeles',
        #     'image': 'static/images/art-expo.jpg',
        #     'price': '$35.00',
        #     'category': 'Art',
        #     'tickets_available': 400,
        #     'organizer': 'Creative Arts Foundation'
        # }
    ]
    
    # Featured events (just the first 3)
    featured_events = events[:3]
    
    # About info
    about_info = {
        'title': 'About Tournament Central',
        'description': 'Tournament Central is the premier platform for event management and tournament hosting. Founded in 2018, we\'ve helped thousands of organizers create memorable experiences for participants and attendees. Our mission is to simplify the process of organizing events while providing cutting-edge tools for registration, ticketing, and real-time updates.',
        'stats': [
            {'number': '500+', 'label': 'Events Hosted'},
            {'number': '50K+', 'label': 'Happy Participants'},
            {'number': '98%', 'label': 'Client Satisfaction'},
            {'number': '24/7', 'label': 'Support Available'}
        ]
    }
    
    # Contact info
    contact_info = {
        'address': '123 Tournament Avenue, Sportsville, SP 54321',
        'phone': '+1 (555) 123-4567',
        'email': 'info@tournamentcentral.com',
        'hours': 'Monday-Friday: 9am to 5pm'
    }
    all_events = Tournament.objects.all()
    context = {
        'all_events': all_events,
        'events': events,
        'featured_events': featured_events,
        'about_info': about_info,
        'contact_info': contact_info,
        'current_year': datetime.now().year
    }
    
    return render(request, 'home.html', context)

def event_detail(request, event_id):
    # Dummy events data (same as in home view)
    current_date = datetime.now()
    submitted = request.session.pop('submitted', False)
    event = Tournament.objects.get(id=event_id)
    if not event:
        # Handle case where event is not found
        return redirect('home')
    
    # Handle form submission
    # if request.method == 'POST':
    #     # In a real application, you would save the form data to a database
    #     # For this example, we'll just simulate a successful submission
        
    #     # Get form data
    #     print(1)
    #     name = request.POST.get('name', '')
    #     email = request.POST.get('email', '')
    #     phone = request.POST.get('phone', '')
    #     tickets = request.POST.get('tickets', 1)
        
    #     print(name, email, phone, tickets)
    #     # Process the uploaded file (in a real app, save it to media storage)
    #     if 'payment_screenshot' in request.FILES:
    #         # Here you would typically save the file
    #         screenshot = request.FILES['payment_screenshot']
    #         # Example of saving file
    #         # file_path = f'payments/{name}_{event_id}_{datetime.now().strftime("%Y%m%d%H%M%S")}.jpg'
    #         # with open(f'{settings.MEDIA_ROOT}/{file_path}', 'wb+') as destination:
    #         #     for chunk in screenshot.chunks():
    #         #         destination.write(chunk)
            
    #     # Generate a mock registration ID
    #     registration_id = datetime.now().strftime("%Y%m%d%H%M%S")
        
    #     # Create registration data (in a real app, this would be saved to the database)
    #     registration_data = {
    #         'id': registration_id,
    #         'name': name,
    #         'email': email,
    #         'phone': phone,
    #         'tickets': tickets,
    #         'event_id': event_id,
    #         'registration_date': datetime.now().strftime("%B %d, %Y %H:%M:%S")
    #     }
        
    #     # Set submitted flag to show success message
    #     submitted = True
        
    #     # In a real application, you would send confirmation emails/SMS here

    #     # Check if this is an AJAX request
    #     is_ajax = request.headers.get('X-Requested-With') == 'XMLHttpRequest'
    #     if is_ajax:
    #         # Return JSON response for AJAX requests
    #         return JsonResponse({
    #             'success': True,
    #             'message': 'Registration successful',
    #             'registration': registration_data
    #         })
            
    #     # Redirect to avoid form resubmission on refresh
    #     # Store registration data in session for retrieval after redirect
    #     request.session['registration_success'] = True
    #     request.session['registration_data'] = registration_data
    #     return redirect('event_detail_success', event_id=event_id)
    
    # Check if redirected after successful registration
    full_name = request.session.pop('full_name', '')
    tournament_name = request.session.pop('tournament_name', '')
    tournament_date = request.session.pop('tournament_date', '')
    context = {
        'event': event,
        'submitted': submitted,
        'current_year': datetime.now().year,
        'full_name': full_name,
        'tournament_name':tournament_name,
        'tournament_date':tournament_date
    }
    
    return render(request, 'events/event_detail.html', context)

def event_detail_success(request, event_id):
    """View shown after successful registration to prevent form resubmission"""
    # Get the success flag and registration data from session
    submitted = request.session.pop('registration_success', False)
    registration_data = request.session.pop('registration_data', None)
    
    if not submitted:
        # If not coming from a successful submission, redirect to the normal event detail page
        return redirect('event_detail', event_id=event_id)
    
    # Get event details as in event_detail view
    current_date = datetime.now()
    
    # Find the event by id
    event = None
    for e in events:
        if e['id'] == event_id:
            event = e
            break
    
    if not event:
        return redirect('home')
    
    context = {
        'event': event,
        'submitted': submitted,
        'registration': registration_data,
        'current_year': datetime.now().year
    }
    
    return render(request, 'events/event_detail.html', context)

# Admin Dashboard Views
# @login_required
def admin_dashboard(request):
    # Mock statistics data
    stats = {
        'total_events': 12,
        'active_events': 5,
        'total_users': 150,
        'new_registrations': 25
    }
    
    # Mock current user data
    current_user = {
        'name': 'Admin User',
        'role': 'Administrator',
        'avatar': 'img/avatar.jpg'
    }
    
    # Mock events data
    events = [
        {'id': 1, 'title': 'Summer Tournament', 'date': '2023-07-15', 'status': 'active', 'registrations': 45},
        {'id': 2, 'title': 'Winter Championship', 'date': '2023-12-10', 'status': 'upcoming', 'registrations': 30},
        {'id': 3, 'title': 'Spring Cup', 'date': '2023-04-22', 'status': 'completed', 'registrations': 60},
    ]
    
    # Mock data for users
    users = [
        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com', 'joined': '2023-01-15', 'status': 'active'},
        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com', 'joined': '2023-02-20', 'status': 'active'},
        {'id': 3, 'name': 'Bob Johnson', 'email': 'bob@example.com', 'joined': '2023-03-05', 'status': 'inactive'},
    ]
    
    # Mock data for registrations
    registrations = [
        {'id': 1, 'user': 'John Doe', 'event': 'Summer Tournament', 'date': '2023-06-10', 'status': 'confirmed'},
        {'id': 2, 'user': 'Jane Smith', 'event': 'Winter Championship', 'date': '2023-11-05', 'status': 'pending'},
        {'id': 3, 'user': 'Bob Johnson', 'event': 'Spring Cup', 'date': '2023-03-15', 'status': 'confirmed'},
    ]
        
    events = Tournament.objects.all()
    context = {
        'stats': stats,
        'current_user': current_user,
        'events': events,
        'users': users,
        'registrations': registrations,
        'active_tab': 'dashboard'
    }
    
    return render(request, 'admin/dashboard.html', context)

# @login_required
def admin_events(request):
    """Admin view for managing events"""
    # Similar to admin_dashboard but with more detailed events data
    # For now, we'll just redirect to the dashboard
    return redirect('admin_dashboard')

def admin_settings(request):
    context = {
        'active_tab': 'settings'
    }
    return render(request, 'admin/settings.html', context)

def admin_reports(request):
    context = {
        'active_tab': 'reports'
    }
    return render(request, 'admin/reports.html', context)

# def admin_verification(request):
#     # Get all events
#     events = Tournament.objects.all()
    
#     # Get participants with payment screenshots
#     verification_requests = Participant.objects.filter(payment_screenshot__isnull=False)
    
#     context = {
#         'verification_requests': verification_requests,
#         'events': events,
#         'active_tab': 'verification'
#     }
    
#     return render(request, 'admin/verification.html', context)

# @login_required
def admin_users(request):
    # Get all users
    users = Participant.objects.all()
    events = Tournament.objects.all()
    context = {
        'users': users,
        'events' : events,
        'active_tab': 'users'
    }
    
    return render(request, 'admin/users.html', context)

@login_required
def admin_registrations(request):
    """Admin view for managing event registrations"""
    # Similar to admin_dashboard but with more detailed registrations data
    # For now, we'll just redirect to the dashboard
    return redirect('admin_dashboard')

# API endpoints for AJAX requests
@login_required
def api_events(request):
    """API endpoint for events data"""
    # Mock events data
    events = [
        {'id': 1, 'name': 'Tech Conference 2023', 'category': 'Conference', 'date': 'Nov 24, 2023', 'location': 'Convention Center, NY', 'status': 'upcoming'},
        {'id': 2, 'name': 'Summer Sports Festival', 'category': 'Sports', 'date': 'Nov 26, 2023', 'location': 'Central Park Stadium', 'status': 'upcoming'},
        {'id': 3, 'name': 'Music Festival 2023', 'category': 'Music', 'date': 'Dec 4, 2023', 'location': 'Riverside Park', 'status': 'upcoming'},
        {'id': 4, 'name': 'Business Summit', 'category': 'Business', 'date': 'Dec 10, 2023', 'location': 'Grand Hotel, Chicago', 'status': 'upcoming'},
        {'id': 5, 'name': 'Food & Wine Expo', 'category': 'Food & Drink', 'date': 'Dec 15, 2023', 'location': 'Exhibition Center', 'status': 'upcoming'}
    ]
    
    return JsonResponse({'events': events})

@login_required
def api_event_detail(request, event_id):
    """API endpoint for single event data"""
    # Mock event data
    event = {
        'id': event_id,
        'name': f'Event {event_id}',
        'description': 'Event description goes here',
        'category': 'Conference',
        'date': 'Nov 24, 2023',
        'time': '9:00 AM',
        'location': 'Convention Center, NY',
        'price': 199.99,
        'capacity': 500,
        'registrations': 45,
        'status': 'upcoming',
        'organizer': 'Event Organizer',
        'featured': True
    }
    
    return JsonResponse({'event': event})

@login_required
def api_users(request):
    """API endpoint for users data"""
    # Mock users data
    users = [
        {'id': 1, 'name': 'John Smith', 'email': 'john@example.com', 'role': 'admin', 'registration_date': 'Jan 15, 2023', 'status': 'active'},
        {'id': 2, 'name': 'Jane Doe', 'email': 'jane@example.com', 'role': 'user', 'registration_date': 'Feb 3, 2023', 'status': 'active'},
        {'id': 3, 'name': 'Robert Johnson', 'email': 'robert@example.com', 'role': 'organizer', 'registration_date': 'Mar 7, 2023', 'status': 'active'},
        {'id': 4, 'name': 'Emily Wilson', 'email': 'emily@example.com', 'role': 'user', 'registration_date': 'Apr 19, 2023', 'status': 'inactive'},
        {'id': 5, 'name': 'Michael Brown', 'email': 'michael@example.com', 'role': 'user', 'registration_date': 'May 22, 2023', 'status': 'active'}
    ]
    
    return JsonResponse({'users': users})

@login_required
def api_user_detail(request, user_id):
    """API endpoint for single user data"""
    # Mock user data
    user = {
        'id': user_id,
        'name': f'User {user_id}',
        'email': f'user{user_id}@example.com',
        'phone': '555-123-4567',
        'address': '123 Main St, City, State',
        'role': 'user',
        'registration_date': 'Jan 15, 2023',
        'status': 'active',
        'last_login': 'Nov 22, 2023'
    }
    
    return JsonResponse({'user': user})

@login_required
def api_registrations(request):
    """API endpoint for registrations data"""
    # Mock registrations data
    registrations = [
        {'id': 1, 'event_name': 'Tech Conference 2023', 'user_name': 'John Smith', 'ticket_type': 'Standard', 'registration_date': 'Nov 10, 2023', 'status': 'confirmed'},
        {'id': 2, 'event_name': 'Summer Sports Festival', 'user_name': 'Jane Doe', 'ticket_type': 'VIP', 'registration_date': 'Nov 12, 2023', 'status': 'confirmed'},
        {'id': 3, 'event_name': 'Music Festival 2023', 'user_name': 'Robert Johnson', 'ticket_type': 'Early Bird', 'registration_date': 'Nov 15, 2023', 'status': 'pending'},
        {'id': 4, 'event_name': 'Business Summit', 'user_name': 'Emily Wilson', 'ticket_type': 'Standard', 'registration_date': 'Nov 18, 2023', 'status': 'confirmed'},
        {'id': 5, 'event_name': 'Food & Wine Expo', 'user_name': 'Michael Brown', 'ticket_type': 'Group', 'registration_date': 'Nov 20, 2023', 'status': 'confirmed'}
    ]
    
    return JsonResponse({'registrations': registrations})

@login_required
def api_registration_detail(request, registration_id):
    """API endpoint for single registration data"""
    # Mock registration data
    registration = {
        'id': registration_id,
        'event_id': 1,
        'event_name': 'Tech Conference 2023',
        'user_id': 2,
        'user_name': 'John Smith',
        'user_email': 'john@example.com',
        'ticket_type': 'Standard',
        'quantity': 2,
        'unit_price': 199.99,
        'total_price': 399.98,
        'registration_date': 'Nov 10, 2023',
        'payment_status': 'paid',
        'status': 'confirmed',
        'notes': 'No special requirements'
    }
    
    return JsonResponse({'registration': registration})

@login_required
def api_stats(request):
    """API endpoint for dashboard statistics"""
    # Mock statistics data
    stats = {
        'total_events': 15,
        'total_users': 253,
        'total_registrations': 154,
        'revenue': 12450,
        'recent_events': [
            {'id': 1, 'name': 'Tech Conference 2023', 'registrations': 45, 'revenue': 8995.5},
            {'id': 2, 'name': 'Summer Sports Festival', 'registrations': 32, 'revenue': 1440},
            {'id': 3, 'name': 'Music Festival 2023', 'registrations': 78, 'revenue': 23322}
        ],
        'recent_users': [
            {'id': 1, 'name': 'John Smith', 'date': 'Nov 21, 2023'},
            {'id': 2, 'name': 'Jane Doe', 'date': 'Nov 20, 2023'},
            {'id': 3, 'name': 'Robert Johnson', 'date': 'Nov 19, 2023'}
        ],
        'monthly_registrations': [65, 59, 80, 81, 56, 90, 102, 85, 95, 110, 120, 154],
        'monthly_revenue': [12000, 19000, 23000, 18000, 25000, 30000, 28000, 26000, 29000, 32000, 35000, 45000]
    }
    
    return JsonResponse({'stats': stats})

# User profile views
@login_required
def user_profile(request):
    """User profile view"""
    # Mock user data
    user = {
        'id': 1,
        'name': 'John Smith',
        'email': 'john@example.com',
        'phone': '555-123-4567',
        'address': '123 Main St, City, State',
        'role': 'user',
        'registration_date': 'Jan 15, 2023'
    }
    
    context = {
        'user': user,
        'current_year': datetime.now().year
    }
    
    return render(request, 'accounts/profile.html', context)

@login_required
def edit_profile(request):
    """Edit user profile view"""
    if request.method == 'POST':
        # Process form data
        # For now, just redirect back to profile
        messages.success(request, 'Profile updated successfully!')
        return redirect('user_profile')
    
    # Mock user data
    user = {
        'id': 1,
        'name': 'John Smith',
        'email': 'john@example.com',
        'phone': '555-123-4567',
        'address': '123 Main St, City, State'
    }
    
    context = {
        'user': user,
        'current_year': datetime.now().year
    }
    
    return render(request, 'accounts/edit_profile.html', context)

@login_required
def user_bookings(request):
    """User bookings/registrations view"""
    # Mock bookings data
    bookings = [
        {'id': 1, 'event_name': 'Tech Conference 2023', 'date': 'Nov 24, 2023', 'ticket_type': 'Standard', 'quantity': 1, 'total': '$199.00', 'status': 'confirmed'},
        {'id': 2, 'event_name': 'Business Summit', 'date': 'Dec 10, 2023', 'ticket_type': 'VIP', 'quantity': 1, 'total': '$449.00', 'status': 'confirmed'},
        {'id': 3, 'event_name': 'Food & Wine Expo', 'date': 'Dec 15, 2023', 'ticket_type': 'Standard', 'quantity': 2, 'total': '$178.00', 'status': 'pending'}
    ]
    
    context = {
        'bookings': bookings,
        'current_year': datetime.now().year
    }
    
    return render(request, 'accounts/bookings.html', context)

@login_required
def booking_detail(request, booking_id):
    """View details of a specific booking"""
    # Mock booking data
    booking = {
        'id': booking_id,
        'event_name': 'Tech Conference 2023',
        'event_date': 'Nov 24, 2023',
        'event_time': '9:00 AM - 5:00 PM',
        'event_location': 'Convention Center, NY',
        'ticket_type': 'Standard',
        'quantity': 1,
        'unit_price': '$199.00',
        'total': '$199.00',
        'booking_date': 'Nov 10, 2023',
        'payment_method': 'Credit Card',
        'payment_status': 'Paid',
        'status': 'confirmed',
        'booking_reference': 'TC2023-001',
        'qr_code': 'static/images/qr-code.png'
    }
    
    context = {
        'booking': booking,
        'current_year': datetime.now().year
    }
    
    return render(request, 'accounts/booking_detail.html', context)

# Additional views needed for URLs
def about(request):
    """About page view"""
    about_info = {
        'title': 'Honest',
        'description': 'Tournament Central is the premier platform for event management and tournament hosting. Founded in 2018, we\'ve helped thousands of organizers create memorable experiences for participants and attendees. Our mission is to simplify the process of organizing events while providing cutting-edge tools for registration, ticketing, and real-time updates.',
        'stats': [
            {'number': '500+', 'label': 'Events Hosted'},
            {'number': '50K+', 'label': 'Happy Participants'},
            {'number': '98%', 'label': 'Client Satisfaction'},
            {'number': '24/7', 'label': 'Support Available'}
        ]
    }
    
    context = {
        'about_info': about_info,
        'current_year': datetime.now().year
    }
    
    return render(request, 'about.html', context)

def contact(request):
    """Contact page view"""
    if request.method == 'POST':
        # Process contact form
        messages.success(request, 'Your message has been sent. We will get back to you soon!')
        return redirect('contact')
    
    contact_info = {
        'address': '123 Tournament Avenue, Sportsville, SP 54321',
        'phone': '+1 (555) 123-4567',
        'email': 'info@tournamentcentral.com',
        'hours': 'Monday-Friday: 9am to 5pm'
    }
    
    context = {
        'contact_info': contact_info,
        'current_year': datetime.now().year
    }
    
    return render(request, 'contact.html', context)

def event_list(request):
    """View to list all events"""
    # Reuse the events data from home view
    current_date = datetime.now()
    
    events = [
        {
            'id': 1,
            'title': 'Tech Conference 2023',
            'description': 'Join industry leaders for a day of innovation and networking in the tech world.',
            'date': (current_date + timedelta(days=5)).strftime('%B %d, %Y'),
            'time': '9:00 AM',
            'location': 'Convention Center, New York',
            'image': '/static/images/image.png',
            'price': '$199.00',
            'category': 'Technology',
            'tickets_available': 500,
            'organizer': 'Tech Events Inc.'
        },
        {
            'id': 2,
            'title': 'Summer Sports Festival',
            'description': 'Annual sports festival featuring various competitions and activities for all ages.',
            'date': (current_date + timedelta(days=7)).strftime('%B %d, %Y'),
            'time': '8:00 AM',
            'location': 'Central Park Stadium',
            'image': 'static/images/sports-festival.jpg',
            'price': '$45.00',
            'category': 'Sports',
            'tickets_available': 1000,
            'organizer': 'Sports Association'
        },
        {
            'id': 3,
            'title': 'Music Festival 2023',
            'description': 'Three days of amazing music performances from top artists around the world.',
            'date': (current_date + timedelta(days=15)).strftime('%B %d, %Y'),
            'time': '2:00 PM',
            'location': 'Riverside Park',
            'image': 'static/images/music-festival.jpg',
            'price': '$299.00',
            'category': 'Music',
            'tickets_available': 2000,
            'organizer': 'Music Events Co.'
        },
        {
            'id': 4,
            'title': 'Business Summit',
            'description': 'Network with industry leaders and learn about the latest business trends.',
            'date': (current_date + timedelta(days=20)).strftime('%B %d, %Y'),
            'time': '10:00 AM',
            'location': 'Grand Hotel, Chicago',
            'image': 'static/images/business-summit.jpg',
            'price': '$349.00',
            'category': 'Business',
            'tickets_available': 300,
            'organizer': 'Business Network'
        },
        {
            'id': 5,
            'title': 'Food & Wine Expo',
            'description': 'Experience the finest culinary delights and premium wines from around the world.',
            'date': (current_date + timedelta(days=25)).strftime('%B %d, %Y'),
            'time': '11:00 AM',
            'location': 'Exhibition Center',
            'image': 'static/images/food-expo.jpg',
            'price': '$89.00',
            'category': 'Food & Drink',
            'tickets_available': 800,
            'organizer': 'Gourmet Events'
        },
        {
            'id': 6,
            'title': 'Art & Design Expo',
            'description': 'Explore creative expressions from talented artists and designers showcasing their innovative work.',
            'date': (current_date + timedelta(days=10)).strftime('%B %d, %Y'),
            'time': '11:00 AM',
            'location': 'Metropolitan Gallery, Los Angeles',
            'image': 'static/images/art-expo.jpg',
            'price': '$35.00',
            'category': 'Art',
            'tickets_available': 400,
            'organizer': 'Creative Arts Foundation'
        }
    ]
    
    # Get category filter from query params
    category = request.GET.get('category', '')
    search = request.GET.get('search', '')
    
    # Apply filters if any
    filtered_events = events
    if category:
        filtered_events = [e for e in events if e['category'].lower() == category.lower()]
    if search:
        search = search.lower()
        filtered_events = [e for e in filtered_events if search in e['title'].lower() or search in e['description'].lower()]
    
    context = {
        'events': filtered_events,
        'categories': ['Technology', 'Sports', 'Music', 'Business', 'Food & Drink', 'Art'],
        'selected_category': category,
        'search_term': search,
        'current_year': datetime.now().year
    }
    
    return render(request, 'events/event_list.html', context)

# Authentication views
def login_view(request):
    """User login view"""
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        # Simple mock authentication
        if username == 'admin' and password == 'password':
            # In a real app, would use Django's authentication system
            return redirect('admin_dashboard')
        elif username and password:
            # Any non-admin user with any credentials
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
    
    return render(request, 'accounts/login.html')

def logout_view(request):
    """User logout view"""
    # In a real app, would use Django's authentication system
    return redirect('home')

def register(request):
    """User registration view"""
    if request.method == 'POST':
        # Process registration form
        messages.success(request, 'Registration successful! You can now log in.')
        return redirect('login')
    
    return render(request, 'accounts/register.html') 


def all_events(request):
    """View to list all events"""
    return render(request, 'events/allevents.html')