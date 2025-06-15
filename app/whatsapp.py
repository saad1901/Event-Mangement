from twilio.rest import Client
from app.models import *

# WhatsApp message sending functionality
def get_message_template(msg_type, name=None, reg_number=None):
    if msg_type == 1:
        return (
            f"*Welcome to Tournament Central!*\n\n"
            f"Thank you for registering, *{name}*.\n"
            "You will receive all updates regarding the tournament here on WhatsApp.\n\n"
            "*Registration Details:*\n"
            f"*Name:* {name}\n"
            f"*Registration Number:* {reg_number}\n\n"  

            "Best of luck!\n-Tournament Central Team"
        )
    elif msg_type == 2:
        return (
            "📢📢📢\n"
            f"Hi *{name}*,\n"
            "This is a reminder for your upcoming tournament. Please check your email for details."
        )
    # Add more types as needed
    else:
        return f"Hello {name}, this is a generic message."

def send_whatsapp_message(user, type=0, media_url=None):
    account_sid = 'AC57048ded5ea9a323f477bffc1aa2af75'
    auth_token = '57cd959d723d959f2fee1a0494f36aa3'
    client = Client(account_sid, auth_token)

    user = Participant.objects.get(id=user)

    phone_number = user.wp
    if not len(phone_number) == 10:
        print("Invalid phone number length. Must be 10 digits.")
        return
    
    message = get_message_template(type, name=user.full_name, reg_number= str(user.registration_id)[:6])
    phone_number = '91'+phone_number
    print(phone_number)
    msg_kwargs = {
        'from_': 'whatsapp:+14155238886',
        'to': f'whatsapp:918799878583',
        'body': message
    }
    # Optionally add media_url if provided
    if media_url:
        msg_kwargs['media_url'] = media_url
    try:
        message_obj = client.messages.create(**msg_kwargs)
    except Exception as e:
        print(f"Failed to send WhatsApp message: {e}")
    print(f"WhatsApp message sent to {phone_number}")

send_whatsapp_message(1,1)
