from twilio.rest import Client

def send_whatsapp_message(phone_number, message, media_url=None):

    client = Client(account_sid, auth_token)
    msg_kwargs = {
        'from_': 'whatsapp:+14155238886',
        'to': f'whatsapp:{phone_number}',
        'body': message
    }
    # Optionally add media_url if provided
    if media_url:
        msg_kwargs['media_url'] = media_url
    message_obj = client.messages.create(**msg_kwargs)
    print(f"WhatsApp message sent to {phone_number}. SID: {message_obj.sid}")

# Example     
if 1 == 11:
  send_whatsapp_message(
    '+918799878583',
    """*Welcome to Tournament Central!*\n
Thank you for registering for the tournament. You will receive all updates and important messages regarding the tournament here on WhatsApp.\n
*Registration Details:*\n
*Name:* John Doe\n
*Registration Number:* 123456\n
If you have any questions, reply to this message.\n
Best of luck!\n
- Tournament Central Team"""
)