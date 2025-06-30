from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from app.models import Tournament, Participant, Transaction
import json
from django.db.models import Count, Sum
from datetime import timedelta

@login_required
def admin_reports(request):
    # Top Events
    top_events_qs = Tournament.objects.annotate(
        registrations=Count('tournament'),
        revenue=Sum('tournament__transaction__amount')
    ).order_by('-registrations')[:5]
    top_events = [
        {
            'title': t.title,
            'registrations': t.registrations or 0,
            'revenue': float(t.revenue or 0),
            'conversion_rate': 100  # Placeholder, implement as needed
        }
        for t in top_events_qs
    ]

    # Active Users
    active_users_qs = User.objects.annotate(
        registrations=Count('organized_tournaments__tournament'),
        total_spent=Sum('organized_tournaments__tournament__transaction__amount')
    ).order_by('-registrations')[:5]
    active_users = [
        {
            'username': u.username,
            'registrations': u.registrations or 0,
            'last_activity': u.last_login or '',
            'total_spent': float(u.total_spent or 0)
        }
        for u in active_users_qs
    ]

    # Monthly Summary (last 30 days)
    now = timezone.now()
    last_month = now - timedelta(days=30)
    monthly_transactions = Transaction.objects.filter(created_at__gte=last_month)
    refunds = monthly_transactions.filter(payment_status='refunded').aggregate(s=Sum('amount'))['s'] or 0
    active_events = Tournament.objects.filter(start_date__gte=now).count()
    # Top city by participant count
    # top_city = Participant.objects.filter(registration_date__gte=last_month).values('city').annotate(c=Count('id')).order_by('-c').first()
    monthly_summary = {
        'revenue': float(monthly_transactions.filter(payment_status='completed').aggregate(s=Sum('amount'))['s'] or 0),
        'revenue_trend': 0,  # Placeholder
        'new_users': User.objects.filter(date_joined__gte=last_month).count(),
        'new_users_trend': 0,  # Placeholder
        'registrations': Participant.objects.filter(registration_date__gte=last_month).count(),
        'registrations_trend': 0,  # Placeholder
        'avg_ticket_price': float(monthly_transactions.aggregate(a=Sum('amount'))['a'] or 0) / (monthly_transactions.count() or 1),
        'avg_ticket_price_trend': 0,  # Placeholder
        'refunds': float(refunds),
        'active_events': active_events,
        # 'top_city': top_city['city'] if top_city else '-',
    }

    # Chart Data
    event_labels = json.dumps([t.title for t in top_events_qs])
    event_registrations = json.dumps([t.registrations or 0 for t in top_events_qs])

    # Revenue Chart Data (real monthly revenue for last 6 months)
    from django.db.models.functions import TruncMonth
    last_6_months = now - timedelta(days=180)
    monthly_revenue_qs = Transaction.objects.filter(
        created_at__gte=last_6_months,
        payment_status='completed'
    ).annotate(month=TruncMonth('created_at')).values('month').annotate(
        total=Sum('amount')
    ).order_by('month')
    revenue_labels = json.dumps([
        m['month'].strftime('%b %Y') for m in monthly_revenue_qs
    ])
    revenue_data = json.dumps([
        float(m['total'] or 0) for m in monthly_revenue_qs
    ])

    reg_trend_labels = json.dumps(['Week 1', 'Week 2', 'Week 3', 'Week 4'])
    reg_trend_data = json.dumps([30, 40, 25, 60])  # Replace with real data if needed

    context = {
        'top_events': top_events,
        'active_users': active_users,
        'monthly_summary': monthly_summary,
        'event_labels': event_labels,
        'event_registrations': event_registrations,
        'revenue_labels': revenue_labels,
        'revenue_data': revenue_data,
        # 'user_dist_labels': user_dist_labels,  # Removed for no pie chart
        # 'user_dist_data': user_dist_data,      # Removed for no pie chart
        'reg_trend_labels': reg_trend_labels,
        'reg_trend_data': reg_trend_data,
        'active_tab': 'reports',
    }
    return render(request, 'admin/reports.html', context)



