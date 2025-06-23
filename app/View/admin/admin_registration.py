from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import JsonResponse, HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from app.models import *
from django.views.decorators.http import require_POST

@login_required
def admin_registration(request):
    events = Tournament.objects.all()
    context = {
        'active_tab': 'registration',
        'events': events,
        'registrations': Participant.objects.all().select_related('tournament'),
    }
    return render(request, 'admin/registrations.html', context)

@login_required
@require_POST
def edit_registration(request, registration_id):
    participant = get_object_or_404(Participant, id=registration_id)
    # Update participant fields from POST data
    participant.full_name = request.POST.get('full_name', participant.full_name)
    participant.email = request.POST.get('email', participant.email)
    participant.phone = request.POST.get('phone', participant.phone)
    participant.wp = request.POST.get('wp', participant.wp)
    participant.age = request.POST.get('age', participant.age)
    participant.gender = request.POST.get('gender', participant.gender)
    participant.status = request.POST.get('status', participant.status)
    participant.notes = request.POST.get('notes', participant.notes)
    participant.special_requirements = request.POST.get('special_requirements', participant.special_requirements)
    # Update event if changed
    event_id = request.POST.get('event_id')
    if event_id:
        participant.tournament = get_object_or_404(Tournament, id=event_id)
    participant.save()

    # Update transaction fields if present
    transaction = getattr(participant, 'transaction', None)
    if transaction:
        transaction.amount = request.POST.get('amount', transaction.amount)
        transaction.payment_status = request.POST.get('payment_status', transaction.payment_status)
        transaction.payment_reference = request.POST.get('payment_reference', transaction.payment_reference)
        transaction.ticket_count = request.POST.get('ticket_count', transaction.ticket_count)
        transaction.ticket_numbers = request.POST.get('ticket_numbers', transaction.ticket_numbers)
        # Handle payment_screenshot file upload
        if 'payment_screenshot' in request.FILES:
            transaction.payment_screenshot = request.FILES['payment_screenshot']
        transaction.save()

    messages.success(request, 'Registration updated successfully.')
    return redirect('admin_registrations')

@login_required
@require_POST
def delete_registration(request, registration_id):
    participant = get_object_or_404(Participant, id=registration_id)
    participant.delete()
    messages.success(request, 'Registration deleted successfully.')
    return redirect('admin_registrations')
