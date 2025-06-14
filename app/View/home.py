from django.shortcuts import render
from datetime import datetime, timedelta
from ..models import Tournament

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
        }
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

def about(request):
    context = {
        'current_year': datetime.now().year
    }
    return render(request, 'about.html', context)

def contact(request):
    context = {
        'current_year': datetime.now().year
    }
    return render(request, 'contact.html', context) 