# File: tests/test_order_creator.py
from lib.order_creator import OrderCreator
from unittest.mock import Mock
import pytest

def test_err_if_empty_menu():
    menu = []
    with pytest.raises(Exception) as err:
        OrderCreator(menu)
    assert str(err.value) == "Menu is empty."

def test_create_order_constructed_with_display_menu_mock():
    mock_menu = Mock()
    mock_menu.display_menu.return_value = {'Pizza': 3.00, 'Pasta': 3.00, 'Steak': 4.00, 'Tuna': 4.00}
    order1 = OrderCreator(mock_menu)
    assert order1.display_formatted_menu() == "Dishes  Prices\nPizza  £3.00\nPasta  £3.00\nSteak  £4.00\nTuna  £4.00"

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
    assert order1.order == {'Pizza': {'Quantity': 2, 'Price': 4.00}}

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
    assert order1.order == {'Pizza': {'Quantity': 2, 'Price': 4.00}, 'Pasta': {'Quantity': 1, 'Price': 3.00}}

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
    assert order1.order == {'Pizza': {'Quantity': 4, 'Price': 8.00}}

def test_itemised_total_for_one_dish_mock():
    mock_menu = Mock()
    mock_menu.display_menu.return_value = {'Pizza': 3.00, 'Pasta': 3.00, 'Steak': 4.00, 'Tuna': 4.00}
    order1 = OrderCreator(mock_menu)
    order1.add_to_order("Pizza", 1)
    assert order1.itemised_total() == "Dishes: 1 Pizza - 3.00\nOrder Total: £3.00"

def test_itemised_total_for_multiple_dish_mock():
    mock_menu = Mock()
    mock_menu.display_menu.return_value = {'Pizza': 3.00, 'Pasta': 3.00, 'Steak': 4.00, 'Tuna': 4.00}

    order1 = OrderCreator(mock_menu)
    order1.add_to_order("Pizza", 1)
    order1.add_to_order("Pasta", 2)
    order1.add_to_order("Steak", 3)
    assert order1.itemised_total() == "Dishes: 1 Pizza - 3.00, 2 Pasta - 6.00, 3 Steak - 12.00\nOrder Total: £21.00"

def test_remove_from_order_removes_dish_mock():
    mock_menu = Mock()
    mock_menu.display_menu.return_value = {'Pizza': 3.00, 'Pasta': 3.00, 'Steak': 4.00, 'Tuna': 4.00}
    order1 = OrderCreator(mock_menu)
    order1.add_to_order("Pizza", 1)
    order1.add_to_order("Pasta", 2)
    order1.add_to_order("Steak", 3)
    order1.remove_from_order("Steak")
    assert order1.itemised_total() == "Dishes: 1 Pizza - 3.00, 2 Pasta - 6.00\nOrder Total: £9.00"

def test_clear_order_and_message_mock():
    mock_menu = Mock()
    mock_menu.display_menu.return_value = {'Pizza': 3.00, 'Pasta': 3.00, 'Steak': 4.00, 'Tuna': 4.00}
    order1 = OrderCreator(mock_menu)
    order1.add_to_order("Pizza", 1)
    order1.add_to_order("Pasta", 2)
    order1.add_to_order("Steak", 3)
    order1.clear_order()
    assert order1.itemised_total() == "Basket is empty."

def test_error_if_clear_order_on_empty_basket():
    mock_menu = Mock()
    mock_menu.display_menu.return_value = {'Pizza': 3.00, 'Pasta': 3.00, 'Steak': 4.00, 'Tuna': 4.00}
    order1 = OrderCreator(mock_menu)
    with pytest.raises(Exception) as err:
        order1.clear_order()
    assert str(err.value) == 'Basket is already empty.'

"""
If #remove_order is called and dish not on order
Raises error
"""
def test_err_remove_if_not_on_order():
    mock_menu = Mock()
    mock_menu.display_menu.return_value = {'Pizza': 3.00, 'Pasta': 3.00, 'Steak': 4.00, 'Tuna': 4.00}
    order1 = OrderCreator(mock_menu)
    order1.add_to_order("Pizza", 1)
    order1.add_to_order("Pasta", 2)
    order1.add_to_order("Steak", 3)

    with pytest.raises(Exception) as err:
        order1.remove_from_order("Tune")
    assert str(err.value) == "Dish not in basket."

"""
If #add_order is called and dish not on menu
Raises error
"""
def test_err_add_if_not_on_menu():
    mock_menu = Mock()
    mock_menu.display_menu.return_value = {'Pizza': 3.00, 'Pasta': 3.00, 'Steak': 4.00, 'Tuna': 4.00}
    order1 = OrderCreator(mock_menu)
    with pytest.raises(Exception) as err:
        order1.add_to_order("Chicken", 1)
    assert str(err.value) == "Dish is not on the menu."
