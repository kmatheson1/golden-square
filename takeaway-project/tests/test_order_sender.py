# File: tests/test_order_sender.py
from lib.order_sender import OrderSender
from unittest.mock import Mock
from datetime import datetime, timedelta

def test_view_receipt_mock():
    mock_order = Mock()
    mock_order.itemised_total.return_value = "Dishes:\n1 Pizza - 3.00\n2 Pasta - 6.00\nOrder Total: £9.00"
    send = OrderSender(mock_order)
    assert send.view_receipt() == "Dishes:\n1 Pizza - 3.00\n2 Pasta - 6.00\nOrder Total: £9.00"

"""
When #time_sent is called
The time that the order was sent is returned
"""
def test_time_sent_mock():
    order1 = Mock()
    send = OrderSender(order1)
    assert send.time_sent() == f'Time Order Sent: {datetime.now().strftime("%H:%M")}'

"""
when #eta is called
string message with estimated time of arrival returned
"""
def test_eta_mock():
    order1 = Mock()
    send = OrderSender(order1)
    assert send.format_eta() == f'Estimated Time of Arrival: {(datetime.now() + timedelta(minutes=30)).strftime("%H:%M")}'