from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Tournament, Category, Transaction, Participant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Sum

#V16
@login_required
def admin_dashboard(request):
    events = Tournament.objects.all()
    total_users = Participant.objects.all().count()
    total_in = Transaction.objects.filter(payment_status = 'completed').aggregate(total=Sum('amount'))['total'] or 0
    context = {
        'events': events,
        'total_users': total_users,
        'total_in': total_in
    }
    return render(request, 'admin/dashboard.html', context)