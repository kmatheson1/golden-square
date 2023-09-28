# File: lib/text_sender.py
from twilio.rest import Client
import os

class TextSender():
    def __init__(self, sent_order):
        self.sent_order = sent_order

    def send_text(self):
        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')

        auth_token  = os.environ.get('TWILIO_AUTH_TOKEN')

        client = Client(account_sid, auth_token)

        eta_time = self.sent_order.eta()

        message = client.messages.create(
            to="+447930367455",
            from_="+447701410106",
            body=f"Thank you! Your order was placed and will be delivered before {eta_time}.")

        print(message.sid)
        return "Message Sent."