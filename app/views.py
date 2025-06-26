from app.models import logModal

def logwrite(sec, id, key, value):
    
    logModal.objects.create(
        sec = sec,
        sec_id = id,
        key = key,
        value = value
    )
    
    
    