# File: tests/test_menu.py
import pytest
from lib.menu_creator import MenuCreator
from unittest.mock import Mock

"""
If no dish has been added
#display_menu returns empty list
"""
def test_empty_list_if_no_dishes():
    menu = MenuCreator()
    assert menu.display_menu() == []

"""
Test dish added to menu as mock
#display_menu returns mock_dish
"""
def test_add_dish_menu_mock():
    menu = MenuCreator()
    dish1 = Mock()
    menu.add_dish_menu(dish1)
    assert menu.display_menu() == [dish1]