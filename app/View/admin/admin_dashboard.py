from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from app.models import Tournament, Category, Transaction, Participant
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Sum

#V26
@login_required
def admin_dashboard(request):
    events = Tournament.objects.all()
    for event in events:
        event.pending_registrations = event.tournament.filter(status='registered').count()
        event.confirmed_registrations = event.tournament.filter(status='confirmed').count()
        # Calculate revenue from confirmed users for this event
        event.revenue_confirmed = sum([
            p.transaction.amount for p in event.tournament.filter(status='confirmed')
            if hasattr(p, 'transaction') and p.transaction.payment_status == 'completed'
        ])
    registered_users = Participant.objects.filter(status = 'confirmed').count()
    pending_users = Participant.objects.filter(status = 'registered').count()
    # Only include transactions for tournaments that still exist
    existing_tournament_ids = Tournament.objects.values_list('id', flat=True)
    total_in = Transaction.objects.filter(payment_status='completed', participant__tournament_id__in=existing_tournament_ids).aggregate(total=Sum('amount'))['total'] or 0
    context = {
        'events': events,
        'pending_users': pending_users,
        'registered_users': registered_users,
        'total_in': total_in,
        'active_tab': 'dashboard',
    }
    return render(request, 'admin/dashboard.html', context)