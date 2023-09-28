# File: lib/test_feature_text_sender.py
from unittest.mock import Mock
from lib.text_sender import TextSender
import pytest

"""
When TextSender is instanciated
A text is sent with an eta 
"""
@pytest.mark.skip(reason="Sends text.")
def test_text_sends_eta():
    sent_order_mock = Mock()
    sent_order_mock.eta.return_value = "18:52"
    confirmation = TextSender(sent_order_mock)
    assert confirmation.send_text() == "Message Sent."
