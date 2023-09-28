# File: lib/order_sender.py
from datetime import datetime, timedelta

class OrderSender():
    def __init__(self, order):
        self._sent_order = order
        self._date_time = datetime.now()

    def view_receipt(self):
        return self._sent_order.itemised_total()

    def time_sent(self):
        return f'Time Order Sent: {self._date_time.strftime("%H:%M")}'
    
    def eta(self):
        eta = self._date_time + timedelta(minutes=30)
        return eta.strftime("%H:%M")

    def format_eta(self):
        eta = self._date_time + timedelta(minutes=30)
        eta_time = eta.strftime("%H:%M")
        return f'Estimated Time of Arrival: {eta_time}'