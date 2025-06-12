from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import *

def admin_events(request):
    events = Tournament.objects.all()
    context = {
        'active_tab': 'events',
        'events': events,
    }
    return render(request, 'admin/events.html', context)