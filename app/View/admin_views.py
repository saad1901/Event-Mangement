from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Tournament, Category, TournamentImage, Participant
from django.contrib.auth.models import User
from django.utils import timezone

@login_required
def admin_settings(request):
    return render(request, 'admin/settings.html')

@login_required
def admin_reports(request):
    return render(request, 'admin/reports.html')

@login_required
def admin_users(request):
    context = {
        'users': Participant.objects.all(),
        'events': Tournament.objects.all(),
        'categories': Category.objects.all(),
    }
    return render(request, 'admin/users.html', context)

