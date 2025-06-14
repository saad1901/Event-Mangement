# Tournament Central - Event Management Platform

## Overview

Tournament Central is a comprehensive event management platform designed to help organizers create, manage, and promote tournaments and events. The platform provides a user-friendly interface for both event organizers and participants, with features for event discovery, registration, ticket management, and more.

## Features

### For Event Organizers

- **Event Creation**: Create and customize events with detailed information including title, description, date, time, location, category, and pricing.
- **Event Management**: Update event details, track registrations, and manage ticket availability.
- **Participant Management**: View and manage participant lists, check-in attendees, and communicate with registered participants.
- **Analytics Dashboard**: Access insights on event performance, ticket sales, and participant demographics.

### For Participants

- **Event Discovery**: Browse events by category, date, or location with an intuitive search and filter system.
- **Registration**: Simple registration process with secure payment options.
- **Ticket Management**: Access digital tickets, view event details, and receive event updates.
- **User Profiles**: Manage personal information and view registration history.

## Technology Stack

- **Backend**: Django (Python web framework)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (development), PostgreSQL (production recommended)
- **Authentication**: Django's built-in authentication system
- **Payment Processing**: Integration-ready for payment gateways

## Project Structure

```
eventapp/
├── app/                  # Main application code
│   ├── View/            # View modules
│   │   ├── __init__.py  # View exports
│   │   ├── home.py      # Home page views
│   │   ├── events.py    # Event-related views
│   │   ├── admin_views.py # Admin dashboard views
│   │   ├── api.py       # API endpoint views
│   │   ├── user.py      # User profile views
│   │   ├── auth.py      # Authentication views
│   │   ├── registration.py # Registration views
│   │   └── verification.py # Verification views
│   ├── models.py        # Database models
│   └── admin.py         # Admin configurations
├── eventapp/            # Project settings
├── media/              # User-uploaded files
├── static/             # Static files
│   ├── css/            # Stylesheets
│   │   ├── main.css    # Main stylesheet
│   │   ├── admin.css   # Admin panel styles
│   │   ├── auth.css    # Authentication pages styles
│   │   ├── events.css  # Event pages styles
│   │   └── profile.css # User profile styles
│   ├── images/         # Image assets
│   └── js/             # JavaScript files
├── templates/          # HTML templates
│   ├── accounts/       # User account templates
│   │   ├── login.html
│   │   ├── register.html
│   │   └── password_reset.html
│   ├── admin/          # Admin panel templates
│   │   ├── dashboard.html
│   │   ├── events.html
│   │   ├── users.html
│   │   └── reports.html
│   ├── events/         # Event-related templates
│   │   ├── event_list.html
│   │   ├── event_detail.html
│   │   └── event_form.html
│   ├── user/           # User profile templates
│   │   ├── profile.html
│   │   ├── edit_profile.html
│   │   └── bookings.html
│   └── base.html       # Base template
├── manage.py           # Django management script
└── db.sqlite3          # Development database
```

## View Structure

### Home Views (`View/home.py`)
- `home()` - Homepage view
- `about()` - About page view
- `contact()` - Contact page view
- Templates: `templates/home.html`, `templates/about.html`, `templates/contact.html`
- CSS: `static/css/main.css`

### Event Views (`View/events.py`)
- `event_detail()` - Event details view
- `event_list()` - List of all events
- `all_events()` - Alternative events listing
- Templates: `templates/events/event_detail.html`, `templates/events/event_list.html`
- CSS: `static/css/events.css`

### Admin Views (`View/admin_views.py`)
- `admin_dashboard()` - Admin dashboard
- `admin_events()` - Event management
- `admin_users()` - User management
- `admin_registrations()` - Registration management
- `admin_settings()` - Admin settings
- `admin_reports()` - Analytics and reports
- Templates: `templates/admin/*.html`
- CSS: `static/css/admin.css`

### API Views (`View/api.py`)
- `api_events()` - Events API endpoint
- `api_event_detail()` - Single event API endpoint
- `api_users()` - Users API endpoint
- `api_user_detail()` - Single user API endpoint
- `api_registrations()` - Registrations API endpoint
- `api_stats()` - Statistics API endpoint

### User Views (`View/user.py`)
- `user_profile()` - User profile view
- `edit_profile()` - Profile editing view
- `user_bookings()` - User's bookings view
- `booking_detail()` - Single booking details
- Templates: `templates/user/*.html`
- CSS: `static/css/profile.css`

### Authentication Views (`View/auth.py`)
- `login_view()` - User login
- `logout_view()` - User logout
- `register()` - User registration
- Templates: `templates/accounts/*.html`
- CSS: `static/css/auth.css`

### Registration Views (`View/registration.py`)
- `addparticipant()` - Add new participant
- `clear_registration_session()` - Clear registration data
- Templates: `templates/registration/*.html`

### Verification Views (`View/verification.py`)
- `admin_verification()` - Verification management
- `update_verification_status()` - Update verification status
- Templates: `templates/admin/verification.html`

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Setup Instructions

1. **Clone the repository**

```bash
git clone <repository-url>
cd eventapp
```

2. **Create and activate a virtual environment**

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up the database**

```bash
python manage.py migrate
```

5. **Create a superuser (admin)**

```bash
python manage.py createsuperuser
```

6. **Run the development server**

```bash
python manage.py runserver
```

7. **Access the application**

Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage Guide

### Admin Panel

1. Navigate to `http://127.0.0.1:8000/admin/`
2. Log in with your superuser credentials
3. Manage events, users, and site content

### Creating an Event

1. Log in to the admin panel
2. Navigate to Events > Add Event
3. Fill in the event details
4. Save the event

### Browsing Events

1. Visit the homepage
2. Browse featured events or use the category filters
3. Click on an event to view details

### Registering for an Event

1. Navigate to the event details page
2. Click the "Register" button
3. Fill in your information
4. Complete the payment process
5. Receive confirmation and digital ticket

## Customization

### Styling

The platform uses a modular CSS structure:
- `main.css` - Global styles and variables
- `admin.css` - Admin panel specific styles
- `auth.css` - Authentication pages styles
- `events.css` - Event-related pages styles
- `profile.css` - User profile pages styles

### Templates

All HTML templates extend from `templates/base.html`. The template structure follows the view organization:
- `accounts/` - Authentication templates
- `admin/` - Admin panel templates
- `events/` - Event-related templates
- `user/` - User profile templates

## Deployment

### Preparing for Production

1. Update `settings.py` with production settings:
   - Set `DEBUG = False`
   - Configure `ALLOWED_HOSTS`
   - Set up a production database

2. Collect static files:

```bash
python manage.py collectstatic
```

3. Set up a production web server (e.g., Nginx, Apache)

4. Configure a WSGI server (e.g., Gunicorn, uWSGI)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support, please contact [support@tournamentcentral.com](mailto:support@tournamentcentral.com) or open an issue in the repository.