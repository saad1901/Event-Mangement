from django.shortcuts import render, get_object_or_404, redirect
from datetime import datetime, timedelta
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from app.models import *
from django.views.decorators.http import require_POST

@login_required
def admin_events(request):
    if request.method == 'POST':
        try:
            # Get form data
            title = request.POST.get('title')
            category_id = request.POST.get('category')
            organizer_id = request.POST.get('organizer')
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')
            tournament_time = request.POST.get('tournament_time')
            registration_deadline = request.POST.get('registration_deadline')
            venue = request.POST.get('venue')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            country = request.POST.get('country')
            postal_code = request.POST.get('postal_code')
            max_participants = request.POST.get('max_participants')
            min_participants = request.POST.get('min_participants')
            entry_fee = request.POST.get('entry_fee')
            prize_pool = request.POST.get('prize_pool')
            tournament_format = request.POST.get('tournament_format')
            rules = request.POST.get('rules')
            status = request.POST.get('status')
            is_featured = request.POST.get('is_featured') == 'on'
            contact_email = request.POST.get('contact_email')
            contact_phone = request.POST.get('contact_phone')
            whatsapp_number = request.POST.get('whatsapp_number')
            facebook_event = request.POST.get('facebook_event')
            instagram_post = request.POST.get('instagram_post')
            description = request.POST.get('description')

            banner_image = request.FILES.get('banner_image')
            additional_images = request.FILES.getlist('additional_images')
            upi_id = request.POST.get('upi_id')
            # Validate required fields
            if not all([
                title, category_id, start_date, registration_deadline, venue, city, state, entry_fee, upi_id
            ]):
                messages.error(request, 'Please fill in all required fields')
                return redirect('admin_events')

            category = Category.objects.get(id=category_id)
            organizer = User.objects.get(id=organizer_id) if organizer_id else None

            tournament = Tournament.objects.create(
                title=title,
                category=category,
                organizer=organizer,
                start_date=start_date,
                end_date=end_date,
                tournament_time=tournament_time,
                registration_deadline=registration_deadline,
                venue=venue,
                address=address,
                city=city,
                state=state,
                country=country,
                postal_code=postal_code,
                max_participants=max_participants,
                min_participants=min_participants or 2,
                entry_fee=entry_fee,
                prize_pool=prize_pool or 0,
                tournament_format=tournament_format,
                rules=rules,
                banner_image=banner_image,
                status=status,
                is_featured=is_featured,
                contact_email=contact_email,
                contact_phone=contact_phone,
                whatsapp_number=whatsapp_number,
                facebook_event=facebook_event,
                instagram_post=instagram_post,
                description=description,
                upi_id=Upis.objects.get(id=upi_id)
            )

            # Handle additional images
            for img in additional_images:
                timg = TournamentImage.objects.create(tournament=tournament, image=img)
                tournament.additional_images.add(timg)

            messages.success(request, 'Event created successfully!')
            
            return redirect('admin_events')
        except Exception as e:
            print(str(e))
            return redirect('admin_events')

    events = Tournament.objects.all()
    for event in events:
        event.revenue_confirmed = sum([
            p.transaction.amount for p in event.tournament.filter(status='confirmed')
            if hasattr(p, 'transaction') and p.transaction.payment_status == 'completed'
        ])
    categories = Category.objects.all()
    context = {
        'events': events,
        'categories': categories,
        'upi_ids': Upis.objects.all(),
        'active_tab': 'events',
    }
    return render(request, 'admin/events.html', context)

@login_required
@require_POST
def admin_event_delete(request, event_id):
    password = request.POST.get('password')
    user = request.user
    if not user.check_password(password):
        messages.error(request, 'Incorrect password. Event not deleted.')
        return redirect('admin_events')
    try:
        event = Tournament.objects.get(id=event_id)
        event.delete()
        messages.success(request, 'Event deleted successfully.')
    except Tournament.DoesNotExist:
        messages.error(request, 'Event not found.')
    return redirect('admin_events')