# File: tests/test_feature_order_sender.py
from lib.dish_creator import DishCreator
from lib.menu_creator import MenuCreator
from lib.order_creator import OrderCreator
from lib.order_sender import OrderSender
from datetime import datetime, timedelta

"""
When instanciated
Receipt for order can be viewed
"""
def test_receipt():
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
    send = OrderSender(order1)
    assert send.view_receipt() == "Dishes: 1 Pizza - 3.00, 2 Pasta - 6.00\nOrder Total: £9.00"

"""
When #time_sent is called
The time that the order was sent is returned
"""
def test_time_sent():
    dish1 = DishCreator("Pizza", 3.00)
    dish2 = DishCreator("Pasta", 3.00)
    menu = MenuCreator()
    menu.add_dish_menu(dish1)
    menu.add_dish_menu(dish2)
    order1 = OrderCreator(menu)
    order1.add_to_order("Pizza", 1)
    order1.add_to_order("Pasta", 2)
    send = OrderSender(order1)
    assert send.time_sent() == f'Time Order Sent: {datetime.now().strftime("%H:%M")}'

"""
when #eta is called
string message with estimated time of arrival returned
"""
def test_eta():
    dish1 = DishCreator("Pizza", 3.00)
    dish2 = DishCreator("Pasta", 3.00)
    menu = MenuCreator()
    menu.add_dish_menu(dish1)
    menu.add_dish_menu(dish2)
    order1 = OrderCreator(menu)
    order1.add_to_order("Pizza", 1)
    order1.add_to_order("Pasta", 2)
    send = OrderSender(order1)
    assert send.eta() == f'Estimated Time of Arrival: {(datetime.now() + timedelta(minutes=30)).strftime("%H:%M")}'