from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.utils import timezone
from app.models import ApiData, Upis, EventData

@login_required
def admin_settings(request):
    org = EventData.objects.filter(id=0).first()
    upis = Upis.objects.all()

    if request.method == 'POST' and 'support_phone' in request.POST:
        
        try:
            if not org:
                EventData.objects.create(
                    name = request.POST.get('site_name'),
                    email = request.POST.get('contact_email'),
                    phone = request.POST.get('support_phone'),
                    wp = request.POST.get('support_wp')
                )
            else:
                org.name = request.POST.get('site_name')
                org.email = request.POST.get('contact_email')
                org.phone = request.POST.get('support_phone')
                org.wp = request.POST.get('support_wp')
                org.save()
            messages.success(request, 'Setting updated successfully.')
            return redirect('admin_settings')
        except:
            messages.error(request, 'Failed to Save Settings')
            return redirect('admin_settings')
        
    elif request.method == 'POST' and 'twilio_sid' in request.POST:
        print("TWilio settings")
        return redirect('admin_settings')

    elif request.method == 'POST' and 'upi_id' in request.POST:
        try:
            Upis.objects.create(
                upi_id = request.POST.get('upi_id'),
                nickname = request.POST.get('nickname'),
                name = request.POST.get('upi_name')
            )
            messages.success(request, 'Setting updated successfully.')
        except:
            messages.error(request, 'Failed to Save Settings')
        return redirect('admin_settings')


    context = {
        'org': org,
        'upis': upis,
        'active_tab': 'settings'
    }
    return render(request, 'admin/settings.html', context)