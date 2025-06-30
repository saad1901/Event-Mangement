from django.shortcuts import render
from app.models import logModal

def logwrite(sec, id, key, value):
    
    logModal.objects.create(
        sec = sec,
        sec_id = id,
        key = key,
        value = value
    )
    
def test(request):
    return render(request, 'events/validate_ticket.html')
    # return render(request, 'events/registration_confirmation.html')