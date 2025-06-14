from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Tournament, Category, TournamentImage, Participant
from django.contrib.auth.models import User
from django.utils import timezone

@login_required
def admin_dashboard(request):
    events = Tournament.objects.all()
    context = {
        'events': events,
    }
    return render(request, 'admin/dashboard.html', context)