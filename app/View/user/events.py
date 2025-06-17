from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import *

def event_detail(request, event_id):
    submitted = request.session.get('submitted', False)
    event = Tournament.objects.get(id=event_id)
    if not event:
        return redirect('home')
    
    full_name = request.session.get('full_name', '')
    tournament_name = request.session.get('tournament_name', '')
    tournament_date = request.session.get('tournament_date', '')
    context = {
        'event': event,
        'submitted': submitted,
        'current_year': datetime.now().year,
        'full_name': full_name,
        'tournament_name': tournament_name,
        'tournament_date': tournament_date
    }
    
    return render(request, 'events/event_detail.html', context)

def event_list(request):
    events = Tournament.objects.all()
    context = {
        'events': events,
        'current_year': datetime.now().year
    }
    return render(request, 'events/event_list.html', context)

def all_events(request):
    events = Tournament.objects.all()
    context = {
        'events': events,
        'current_year': datetime.now().year
    }
    return render(request, 'events/allevents.html', context)