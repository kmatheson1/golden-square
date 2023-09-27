# File: tests/test_order_creator.py
from lib.order_creator import OrderCreator
from unittest.mock import Mock

def test_create_order_constructed_with_display_menu_mock():
    dish1 = Mock()
    dish2 = Mock()
    dish3 = Mock()
    menu = Mock()
    menu.display_menu.return_value = {dish1.dish: dish1.price, dish2.dish: dish2.price, dish3.dish: dish3.price}
    order1 = OrderCreator(menu)
    order1.menu = {dish1.dish: dish1.price, dish2.dish: dish2.price, dish3.dish: dish3.price}
    assert order1.menu == menu.display_menu()

"""
If add_dish_menu one dish to order
#self.order stores the order as a nested dict
"""
def test_add_order_adds_to_order_mock():
    mock_menu = Mock()
    mock_menu.display_menu.return_value = {'Pizza': 2.00, 'Pasta': 3.00, 'Steak': 4.00, 'Tuna': 4.00}
    order1 = OrderCreator(mock_menu)
    order1.add_to_order("Pizza", 1)
    assert order1.order == {'Pizza': {'Quantity': 1, 'Price': 2.00}}

"""
If add_dish_menu multiple of same dish
Quantity is reflected in order
"""
def test_add_order_adds_multiple_to_order_mock():
    mock_menu = Mock()
    mock_menu.display_menu.return_value = {'Pizza': 2.00, 'Pasta': 3.00, 'Steak': 4.00, 'Tuna': 4.00}
    order1 = OrderCreator(mock_menu)
    order1.add_to_order("Pizza", 2)
    assert order1.order == {'Pizza': {'Quantity': 2, 'Price': 2.00}}

"""
If multiple and different dishes added to order
reflected in order
"""
def test_add_order_adds_multiple_different_to_order_mock():
    mock_menu = Mock()
    mock_menu.display_menu.return_value = {'Pizza': 2.00, 'Pasta': 3.00, 'Steak': 4.00, 'Tuna': 4.00}
    order1 = OrderCreator(mock_menu)
    order1.add_to_order("Pizza", 2)
    order1.add_to_order("Pasta", 1)
    assert order1.order == {'Pizza': {'Quantity': 2, 'Price': 2.00}, 'Pasta': {'Quantity': 1, 'Price': 3.00}}

"""
If dish added to order twice
order will update quantity
"""
def test_dish_added_twice_updates_quantity_mock():
    mock_menu = Mock()
    mock_menu.display_menu.return_value = {'Pizza': 2.00, 'Pasta': 3.00, 'Steak': 4.00, 'Tuna': 4.00}
    order1 = OrderCreator(mock_menu)
    order1.add_to_order("Pizza", 2)
    order1.add_to_order("Pizza", 2)
    assert order1.order == {'Pizza': {'Quantity': 4, 'Price': 2.00}}