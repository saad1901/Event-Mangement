from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import *
from django.http import JsonResponse
from django.views.decorators.http import require_POST
import json
from django.views.decorators.csrf import csrf_exempt
from app.View.msg.whatsapp import send_whatsapp_message

def admin_verification(request):
    alltournaments = Tournament.objects.all()
    verification_requests = Participant.objects.filter(status='registered')
    context = {
        'verification_requests': verification_requests,
        # 'events': events,
        'active_tab': 'verification',
        'alltournaments': alltournaments,
    }
    
    return render(request, 'admin/verification.html', context)

@csrf_exempt  # Optional: only use this if not handling CSRF token in frontend
@require_POST
def update_verification_status(request, request_id):
    try:
        data = json.loads(request.body)
        action = data.get('action')
        reason = data.get('reason', '')
        verification = Participant.objects.get(id=request_id)
        transaction = verification.transaction
        if not transaction:
            return JsonResponse({'message': 'Transaction not found.'}, status=404)
        print(transaction.payment_status)
        if action == 'accept':
            verification.status = 'confirmed'
            transaction.payment_status = 'completed'
            send_whatsapp_message(verification,2)
        elif action == 'reject':
            verification.status = 'rejected'
            transaction.payment_status = 'failed'
            send_whatsapp_message(verification,3,reason=reason)
        elif action == 'review':
            verification.status = 'under_review'
            transaction.payment_status = 'pending'
        else:
            return JsonResponse({'message': 'Invalid action'}, status=400)

        verification.save()
        transaction.save()
        return JsonResponse({'message': f"Request marked as {verification.status}."})

    except Participant.DoesNotExist:
        return JsonResponse({'message': 'Request not found.'}, status=404)
    except Exception as e:
        return JsonResponse({'message': f'Error: {str(e)}'}, status=500)
