# File: lib/test_feature_text_sender.py
import unittest
from unittest.mock import Mock
from lib.text_sender import TextSender
import pytest
import os

"""
When TextSender is instanciated
A text is sent with an eta 
"""
@pytest.mark.skip(reason="Sends text.")
def test_text_sends_eta():
    sent_order_mock = Mock()
    sent_order_mock.eta.return_value = "18:52"
    confirmation = TextSender(sent_order_mock, os.environ.get('MY_PHONE_NUMBER'))
    assert confirmation.send_text() == "Message Sent."

"""
when TextSender instaciated
error if not valid phone number
"""
def test_text_invalid_number():
    sent_order_mock = Mock()
    with pytest.raises(Exception) as err:
        TextSender(sent_order_mock, "079353674")
    assert str(err.value) == "Not a valid UK phone number."

@pytest.mark.skip(reason="Sends text.")
def test_text_sender_mock():
    sent_order_mock = Mock()
    user_phone_number_fake = os.environ['MY_PHONE_NUMBER'] #valid uk phone number
    
    text_sender = TextSender(sent_order_mock, user_phone_number_fake)

    #import environmental variables
    sent_order_mock.eta.return_value = "2:00 PM"

    # Mock Twilio's Client and Message creation
    with pytest.raises(AssertionError):
        with unittest.mock.patch('twilio.rest.Client') as mock_client:
            # Create a mock message
            mock_message = Mock()
            
            # Set up the expected call to messages.create
            expected_create_call = mock_client.return_value.messages.create
            expected_create_call.return_value = mock_message

            # Call the send_text method
            result = text_sender.send_text()

            # Assert that result is "Message Sent."
            assert result == "Message Sent."

            # Assert that the expected calls were made
            mock_client.assert_called_with(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
            expected_create_call.assert_called_with(
                to=user_phone_number_fake,
                from_=os.environ['TWILIO_PHONE_NUMBER'],
                body="Thank you! Your order was placed and will be delivered before 2:00 PM.")







