from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import Tournament

@login_required
def api_events(request):
    events = Tournament.objects.all()
    data = [{'id': event.id, 'title': event.title} for event in events]
    return JsonResponse({'events': data})

@login_required
def api_event_detail(request, event_id):
    event = Tournament.objects.get(id=event_id)
    data = {
        'id': event.id,
        'title': event.title,
        'description': event.description,
        'date': event.date,
        'location': event.location
    }
    return JsonResponse(data)

@login_required
def api_users(request):
    return JsonResponse({'message': 'API endpoint for users'})

@login_required
def api_user_detail(request, user_id):
    return JsonResponse({'message': f'API endpoint for user {user_id}'})

@login_required
def api_registrations(request):
    return JsonResponse({'message': 'API endpoint for registrations'})

@login_required
def api_registration_detail(request, registration_id):
    return JsonResponse({'message': f'API endpoint for registration {registration_id}'})

@login_required
def api_stats(request):
    return JsonResponse({'message': 'API endpoint for statistics'}) 