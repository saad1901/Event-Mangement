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

## Project Structure

```
eventapp/
├── app/                  # Main application code
├── eventapp/             # Project settings
├── media/                # User-uploaded files
├── static/               # Static files (CSS, JS, images)
│   ├── css/              # Stylesheets
│   ├── images/           # Image assets
│   └── js/               # JavaScript files
├── staticfiles/          # Collected static files for production
├── templates/            # HTML templates
│   ├── accounts/         # User account templates
│   ├── admin/            # Admin panel templates
│   ├── events/           # Event-related templates
│   └── base.html         # Base template
├── manage.py             # Django management script
└── db.sqlite3            # Development database
```

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

The platform uses a modern, responsive design system with customizable components. The main stylesheet is located at `static/css/styles.css` and includes variables for colors, typography, and spacing that can be adjusted to match your branding.

### Templates

All HTML templates extend from `templates/base.html`. You can modify this file to change the global layout, navigation, and footer.

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