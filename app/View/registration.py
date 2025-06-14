from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import *

@login_required
def admin_registration(request):
    events = Tournament.objects.all()
    # registrations = Participant.objects.all()
    context = {
        'active_tab': 'registration',
        'events': events,
        'registrations': Participant.objects.all(),
    }

    return render(request, 'admin/registrations.html', context)
