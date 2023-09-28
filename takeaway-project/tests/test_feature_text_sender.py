# File: lib/test_feature_text_sender.py
from lib.dish_creator import DishCreator
from lib.menu_creator import MenuCreator
from lib.order_creator import OrderCreator
from lib.order_sender import OrderSender
from lib.text_sender import TextSender
import pytest

"""
If send_text is called
Text with eta will be sent
"""
#@pytest.mark.skip(reason="Sends text.")
def test_send_text():
    dish1 = DishCreator("Pizza", 3.00)
    dish2 = DishCreator("Pasta", 3.00)
    dish3 = DishCreator("Steak", 4.00)
    dish4 = DishCreator("Tuna", 4.00)
    menu = MenuCreator()
    menu.add_dish_menu(dish1)
    menu.add_dish_menu(dish2)
    menu.add_dish_menu(dish3)
    menu.add_dish_menu(dish4)
    order1 = OrderCreator(menu)
    order1.add_to_order("Pizza", 1)
    order1.add_to_order("Pasta", 2)
    send_order = OrderSender(order1)
    confirmation = TextSender(send_order)
    assert confirmation.send_text() == "Message Sent."
