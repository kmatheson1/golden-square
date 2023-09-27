# File: tests/test_menu.py
import pytest
from lib.menu_creator import MenuCreator
from unittest.mock import Mock

"""
If no dish has been added
#display_menu returns empty dict
"""
def test_empty_list_if_no_dishes():
    menu = MenuCreator()
    assert menu.display_menu() == {}

"""
Test dish added to menu as mock
#display_menu returns mock_dish
"""
def test_add_dish_menu_mock():
    menu = MenuCreator()
    mock_dish1 = Mock()
    mock_dish1.dish = "Pizza"
    mock_dish1.price = 2.00
    menu.add_dish_menu(mock_dish1)
    assert menu.display_menu() == {mock_dish1.dish: mock_dish1.price}

"""
When #display_menu called
Only available dishes are returned
"""
def test_display_menu_only_available_dishes_mock():
    mock_dish1 = Mock()
    mock_dish2 = Mock()
    menu = MenuCreator()
    menu.add_dish_menu(mock_dish1)
    menu.add_dish_menu(mock_dish2)
    mock_dish1.available = False
    mock_dish2.available = True
    assert menu.display_menu() == {mock_dish2.dish: mock_dish2.price}

"""
If #remove_dish is called
Dish will not be displayed in #display_menu
"""
def test_remove_dish_from_menu():
    dish1 = Mock()
    dish2 = Mock()
    dish3 = Mock()
    menu = MenuCreator()
    menu.add_dish_menu(dish1)
    menu.add_dish_menu(dish2)
    menu.add_dish_menu(dish3)
    menu.remove_dish(dish1)
    assert menu.display_menu() == {dish2.dish: dish2.price, dish3.dish: dish3.price}