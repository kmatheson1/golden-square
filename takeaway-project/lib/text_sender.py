# File: lib/text_sender.py
from twilio.rest import Client
import os
import re

class TextSender():
    def __init__(self, sent_order, user_phone_number):
        self._sent_order = sent_order

        #raises error if TextSender called with invalid UK phone number
        if self.is_valid_uk_phone_number(user_phone_number):
            self._user_phone_number = user_phone_number
        else:
            raise Exception("Not a valid UK phone number.")

    def is_valid_uk_phone_number(self, phone_number):
        #expression pattern to check for valid uk phone number
        pattern = r'^(?:\+44|0[1-9]\d{9}|07\d{9})'
        return bool(re.match(pattern, phone_number))

    def send_text(self):
        #Twilio API will send text with users estimated time of delivery.

        account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
        auth_token  = os.environ.get('TWILIO_AUTH_TOKEN')
        phone_number = os.environ.get('TWILIO_PHONE_NUMBER')
        eta_time = self._sent_order.eta()

        client = Client(account_sid, auth_token)
        message = client.messages.create(
            to=self._user_phone_number,
            from_=phone_number,
            body=f"Thank you! Your order was placed and will be delivered before {eta_time}.")
        
        message
        return "Message Sent."