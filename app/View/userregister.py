from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import *

def addparticipant(request):
    submitted = request.session.pop('submitted', False)
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
                age=request.POST.get('age'),
                gender=request.POST.get('gender'),
                notes=request.POST.get('notes', ''),
                registration_date=datetime.now()
            )

            # Save Transaction first
            transactionData = Transaction(
                amount=request.POST.get('amount'),
                payment_screenshot=request.FILES.get('payment_screenshot'),
                ticket_count=request.POST.get('tickets'),
            )
            transactionData.save()

            # Assign transaction to participant
            participant.transaction = transactionData
            participant.save()

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
            request.session['tournament_date'] = tournament.start_date

            return redirect('event_detail', event_id=event_id)

        except Exception as e:
            print(f"Error occurred: {e}")
            # Redirect or handle error as needed
            return redirect('home')

    if not tournament:
        # If GET or tournament not found
        event_id = request.GET.get('event_id')
        if event_id:
            tournament = get_object_or_404(Tournament, id=event_id)
        else:
            return redirect('home')

    context = {
        'event': tournament,
        'submitted': submitted,
        'current_year': datetime.now().year
    }

    return render(request, 'events/event_detail.html', context)


def clear_registration_session(request):
    keys_to_clear = ['submitted', 'full_name', 'tournament_name', 'tournament_date']
    for key in keys_to_clear:
        request.session.pop(key, None)
    return redirect('event_detail', event_id=request.POST.get('event_id'))  # Replace 'register' with your form URL name
