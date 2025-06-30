from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import *
from ..msg import *
from django.db import transaction as db_transaction

def addparticipant(request):
    submitted = request.session.get('submitted', False)
    tournament = None  # default in case of non-POST

    if request.method == 'POST':
        try:
            event_id = request.POST.get('event_id')
            tournament = get_object_or_404(Tournament, id=event_id)

            # Create Participant instance but don't save yet
            participant = Participant(
                tournament=tournament,
                full_name=request.POST.get('full_name'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone'),
                wp=request.POST.get('wp'),
                age=request.POST.get('age'),
                gender=request.POST.get('gender'),
                notes=request.POST.get('notes', ''),
                registration_date=datetime.now(),
            )
            # Save Transaction first, but only commit if participant saves successfully
            try:
                amount = float(tournament.entry_fee)
                ticket_count = int(request.POST.get('tickets', 1))
            except (TypeError, ValueError):
                amount = 0
                ticket_count = 1
            total_amount = amount * ticket_count
            with db_transaction.atomic():
                transactionData = Transaction(
                    amount=total_amount,
                    ticket_count=ticket_count,
                    payment_screenshot=request.FILES.get('payment_screenshot'),
                )
                transactionData.save()
                # Assign transaction to participant
                participant.transaction = transactionData
                try:
                    participant.save()
                except Exception as e:
                    # If participant fails to save, add error message and redirect
                    messages.error(request, 'Participant could not be saved. Try Again.')
                    return redirect('event_detail', event_id=event_id)

            # Save ChessPlayer data if the category is chess
            if tournament.category == 1:
                chessData = ChessPlayer(
                    participant=participant,
                    fide_id=request.POST.get('fide_id', ''),
                    fide_rating=request.POST.get('fide_rating') or None,
                    national_rating=request.POST.get('national_rating') or None,
                    title=request.POST.get('title', ''),
                    federation=request.POST.get('federation'),
                    section=request.POST.get('section'),
                    club=request.POST.get('club', ''),
                )
                chessData.save()

            request.session['submitted'] = True
            request.session['full_name'] = request.POST.get('full_name')
            request.session['tournament_name'] = tournament.title
            request.session['tournament_date'] = str(tournament.start_date)
            request.session['registration_id'] = str(participant.registration_id)[:5]

            send_whatsapp_message(participant, 1)

            return redirect('event_detail', event_id=event_id)

        except Exception as e:
            print(f"Error occurred: {e}")
            messages.error(request, str(e) or 'Try Again')
            return redirect('event_detail', event_id=event_id)

    if not tournament:
        # If GET or tournament not found
        event_id = request.GET.get('event_id')
        if event_id:
            tournament = get_object_or_404(Tournament, id=event_id)
        else:
            return redirect('event_detail', event_id=event_id)

    # context = {
    #     'event': tournament,
    #     'submitted': submitted,
    #     'current_year': datetime.now().year
    # }

    # return render(request, 'events/event_detail.html', context)


def clear_registration_session(request):
    keys_to_clear = ['submitted', 'full_name', 'tournament_name', 'tournament_date']
    for key in keys_to_clear:
        request.session.pop(key, None)
    return redirect('event_detail', event_id=request.POST.get('event_id'))  # Replace 'register' with your form URL name
