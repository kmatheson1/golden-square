# File: lib/text_sender.py
from twilio.rest import Client
import os

class TextSender():
    def __init__(self, sent_order, user_phone_number):
        self._sent_order = sent_order
        self._user_phone_number = user_phone_number

    def send_text(self):
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth_token  = os.environ.get('TWILIO_AUTH_TOKEN')

        client = Client(account_sid, auth_token)

        eta_time = self._sent_order.eta()

        phone_number = os.environ.get('TWILIO_PHONE_NUMBER')

        message = client.messages.create(
            to=self._user_phone_number,
            from_=phone_number,
            body=f"Thank you! Your order was placed and will be delivered before {eta_time}.")

        print(message.sid)
        return "Message Sent."