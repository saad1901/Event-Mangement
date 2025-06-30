from django.shortcuts import render
from datetime import datetime, timedelta
from app.models import Tournament, EventData

def home(request):
    # Dummy events data
    current_date = datetime.now()
    data = EventData.objects.order_by('-id').first()
    all_events = Tournament.objects.all()
    context = {
        'all_events': all_events,
        'upcoming_events': all_events,
        'featured_events': Tournament.objects.filter(is_featured=True),
        'current_year': datetime.now().year,
        'data': data,
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