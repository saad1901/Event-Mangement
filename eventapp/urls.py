from django.contrib import admin as django_admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app.View import *
from app import views
urlpatterns = [
    # Django admin
    path('admin/', django_admin.site.urls),
    
    # Main site URLs
    path('', home, name='home'),
    path('home/allevents/', all_events, name='all_events'),
    path('home/event/<int:event_id>/', event_detail, name='event_detail'),
    path('home/about/', about, name='about'),
    path('home/contact/', contact, name='contact'),
    path('home/events/', event_list, name='event_list'),
    path('test', views.test, name='event_list'),
    
    # Authentication URLs
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),
    path('auth/register/', register, name='register'),
    path('auth/password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('auth/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('auth/password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('auth/password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    
    # Admin Dashboard URLs
    path('superadmin/dashboard/', admin_dashboard, name='admin_dashboard'),
    path('superadmin/dashboard/events/', admin_events, name='admin_events'),
    path('superadmin/dashboard/users/', admin_users, name='admin_users'),
    path('superadmin/dashboard/registrations/', admin_registration, name='admin_registrations'),
    path('superadmin/dashboard/verification/', admin_verification, name='admin_verification'),
    path('superadmin/dashboard/settings/', admin_settings, name='admin_settings'),
    path('superadmin/dashboard/reports/', admin_reports, name='admin_reports'),
    path('superadmin/dashboard/admin_downloads/', downloads_home, name='admin_downloads'),
    path('superadmin/dashboard/admin_downloads/export/', export_participants_csv, name='export_participants_csv'),
    path('superadmin/dashboard/addparticipant/', addparticipant, name='addparticipant'),
    path('superadmin/dashboard/clear-registration/', clear_registration_session, name='clear_registration_session'),
    path('superadmin/dashboard/editregistration/<int:registration_id>/', edit_registration, name='edit_registration'),
    path('superadmin/dashboard/deleteregistration/<int:registration_id>/', delete_registration, name='delete_registration'),

    # Admin API endpoints for AJAX requests
    path('superadmin/api/events/', api_events, name='api_events'),
    path('superadmin/api/events/<int:event_id>/', api_event_detail, name='api_event_detail'),
    path('superadmin/api/users/', api_users, name='api_users'),
    path('superadmin/api/users/<int:user_id>/', api_user_detail, name='api_user_detail'),
    path('superadmin/api/registrations/', api_registrations, name='api_registrations'),
    path('superadmin/api/registrations/<int:registration_id>/', api_registration_detail, name='api_registration_detail'),
    path('superadmin/api/stats/', api_stats, name='api_stats'),
    path('superadmin/api/verification/update-status/<int:request_id>/', update_verification_status, name='update_verification_status'),

    # User profile and bookings
    path('user/profile/', user_profile, name='user_profile'),
    path('user/profile/edit/', edit_profile, name='edit_profile'),
    path('user/profile/bookings/', user_bookings, name='user_bookings'),
    path('user/profile/bookings/<int:booking_id>/', booking_detail, name='booking_detail'),
]

# Add static and media serving for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
