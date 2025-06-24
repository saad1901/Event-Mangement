from twilio.rest import Client
from app.models import *
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

# WhatsApp message sending functionality
def get_message_template(msg_type, reason=None, name=None, reg_number=None, event_name=None, event_date=None):
    reg_number_display = str(reg_number)[:5] if reg_number else "-----"
    event_line = f"*Tournament:* {event_name}\n" if event_name else ""
    date_line = f"*Date:* {event_date}\n" if event_date else ""
    if msg_type == 1:
        return (
            f"*🎉 Welcome to Tournament Central!*\n\n"
            f"Dear *{name}*,\n"
            "Thank you for registering for our tournament. You will receive all updates here on WhatsApp.\n\n"
            "*Registration Details:*\n"
            f"*Name:* {name}\n"
            f"*Registration No.:* {reg_number_display}\n"
            f"{event_line}"
            f"{date_line}"
            "\nWe wish you the best of luck!\n\n"
            "Regards,\nTournament Central Team"
        )
    elif msg_type == 2:
        return (
            f"*✅ Registration Confirmed!*\n\n"
            f"Hello *{name}*,\n"
            "Your registration for the tournament has been *confirmed*.\n\n"
            "*Registration Details:*\n"
            f"*Name:* {name}\n"
            f"*Registration No.:* {reg_number_display}\n"
            f"{event_line}"
            f"{date_line}"
            "\nWe look forward to seeing you at the event!\n\n"
            "Regards,\nTournament Central Team"
        )
    elif msg_type == 3:
        return (
            f"*❌ Registration Rejected*\n\n"
            f"Hello *{name}*,\n"
            "We regret to inform you that your registration for the tournament has been *rejected*.\n\n"
            "*Registration Details:*\n"
            f"*Name:* {name}\n"
            f"*Registration No.:* {reg_number_display}\n"
            f"{event_line}"
            f"{date_line}"
            f"*Reason:* {reason}\n\n"
            "If you have any questions, please contact us.\n\n"
            "Regards,\nTournament Central Team"
        )
    # Add more types as needed
    else:
        return f"Hello {name}, this is a generic message from Tournament Central."

def send_whatsapp_message(user, type=0, reason=None, media_url=None):
    client = Client(account_sid, auth_token)

    phone_number = user.wp
    if not len(phone_number) == 10:
        print("Invalid phone number length. Must be 10 digits.")
        return

    # Get event name and date if available
    event_name = getattr(user.tournament, 'title', None) if hasattr(user, 'tournament') else None
    event_date = getattr(user.tournament, 'date', None) if hasattr(user, 'tournament') else None

    message = get_message_template(
        type,
        reason=reason,
        name=user.full_name,
        reg_number=str(user.registration_id)[:5],
        event_name=event_name,
        event_date=event_date
    )
    print(message)
    phone_number = '91'+phone_number
    print(phone_number)
    msg_kwargs = {
        'from_': 'whatsapp:+14155238886',
        'to': f'whatsapp:918799878583',
        'body': message
    }
    if media_url:
        msg_kwargs['media_url'] = media_url
    try:
        message_obj = client.messages.create(**msg_kwargs)
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")
    print(f"WhatsApp message sent to {phone_number}")
