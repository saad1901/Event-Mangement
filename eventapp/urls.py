from django.contrib import admin as django_admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app.View import *

urlpatterns = [
    # Django admin
    path('admin/', django_admin.site.urls),
    
    # Main site URLs
    path('', home, name='home'),
    path('allevents/', all_events, name='all_events'),
    path('event/<int:event_id>/', event_detail, name='event_detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('events/', event_list, name='event_list'),
    
    # Authentication URLs
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    
    # Admin Dashboard URLs
    path('dashboard/', admin_dashboard, name='admin_dashboard'),
    path('dashboard/events/', admin_events, name='admin_events'),
    path('dashboard/users/', admin_users, name='admin_users'),
    path('dashboard/registrations/', admin_registration, name='admin_registrations'),
    path('dashboard/verification/', admin_verification, name='admin_verification'),
    path('dashboard/settings/', admin_settings, name='admin_settings'),
    path('dashboard/reports/', admin_reports, name='admin_reports'),
    path('addparticipant/', addparticipant, name='addparticipant'),
    path('clear-registration/', clear_registration_session, name='clear_registration_session'),
    path('editregistration/<int:registration_id>/', edit_registration, name='edit_registration'),
    path('deleteregistration/<int:registration_id>/', delete_registration, name='delete_registration'),

    # Admin API endpoints for AJAX requests
    path('api/events/', api_events, name='api_events'),
    path('api/events/<int:event_id>/', api_event_detail, name='api_event_detail'),
    path('api/users/', api_users, name='api_users'),
    path('api/users/<int:user_id>/', api_user_detail, name='api_user_detail'),
    path('api/registrations/', api_registrations, name='api_registrations'),
    path('api/registrations/<int:registration_id>/', api_registration_detail, name='api_registration_detail'),
    path('api/stats/', api_stats, name='api_stats'),
    path('api/verification/update-status/<int:request_id>/', update_verification_status, name='update_verification_status'),

    # User profile and bookings
    path('profile/', user_profile, name='user_profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('profile/bookings/', user_bookings, name='user_bookings'),
    path('profile/bookings/<int:booking_id>/', booking_detail, name='booking_detail'),
]

# Add static and media serving for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
