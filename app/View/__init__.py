from .events import *
from .verification import *
from .registration import *
from .userregister import *

# Import views from their respective modules
from .home import home, about, contact
from .events import event_detail, event_list, all_events
from .admin_views import (
    admin_dashboard, admin_events, admin_settings,
    admin_reports, admin_users, admin_registrations
)
from .api import (
    api_events, api_event_detail, api_users,
    api_user_detail, api_registrations,
    api_registration_detail, api_stats
)
from .user import (
    user_profile, edit_profile,
    user_bookings, booking_detail
)
from .auth import login_view, logout_view, register

# # Export all views
# __all__ = [
#     'home', 'about', 'contact',
#     'event_detail', 'event_list', 'all_events',
#     'admin_dashboard', 'admin_events', 'admin_settings',
#     'admin_reports', 'admin_users', 'admin_registrations',
#     'api_events', 'api_event_detail', 'api_users',
#     'api_user_detail', 'api_registrations',
#     'api_registration_detail', 'api_stats',
#     'user_profile', 'edit_profile',
#     'user_bookings', 'booking_detail',
#     'login_view', 'logout_view', 'register'
# ]
