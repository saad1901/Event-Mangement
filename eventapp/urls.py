"""
URL configuration for eventapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from app.View import *
urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),
    
    # Main site URLs
    path('', views.home, name='home'),
    path('allevents/', views.all_events, name='all_events'),
    path('event/<int:event_id>/', views.event_detail, name='event_detail'),
    # path('event/<int:event_id>/success/', views.event_detail_success, name='event_detail_success'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('events/', views.event_list, name='event_list'),
    
    # Authentication URLs
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='accounts/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'), name='password_reset_complete'),
    
    # Admin Dashboard URLs
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/events/', admin_events, name='admin_events'),
    path('dashboard/users/', views.admin_users, name='admin_users'),
    path('dashboard/registrations/', admin_registration, name='admin_registrations'),
    path('dashboard/verification/', admin_verification, name='admin_verification'),
    path('dashboard/settings/', views.admin_settings, name='admin_settings'),
    path('dashboard/reports/', views.admin_reports, name='admin_reports'),
    path('addparticipant/', addparticipant, name='addparticipant'),
    path('clear-registration/', clear_registration_session, name='clear_registration_session'),





    # Admin API endpoints for AJAX requests
    path('api/events/', views.api_events, name='api_events'),
    path('api/events/<int:event_id>/', views.api_event_detail, name='api_event_detail'),
    path('api/users/', views.api_users, name='api_users'),
    path('api/users/<int:user_id>/', views.api_user_detail, name='api_user_detail'),
    path('api/registrations/', views.api_registrations, name='api_registrations'),
    path('api/registrations/<int:registration_id>/', views.api_registration_detail, name='api_registration_detail'),
    path('api/stats/', views.api_stats, name='api_stats'),
    path('api/verification/update-status/<int:request_id>/', update_verification_status, name='update_verification_status'),

    # User profile and bookings
    path('profile/', views.user_profile, name='user_profile'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
    path('profile/bookings/', views.user_bookings, name='user_bookings'),
    path('profile/bookings/<int:booking_id>/', views.booking_detail, name='booking_detail'),
]

# Add static and media serving for development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
