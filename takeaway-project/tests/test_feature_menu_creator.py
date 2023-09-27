# File: tests/test_integration_takeaway.py
import pytest
from lib.menu_creator import MenuCreator
from lib.dish_creator import DishCreator

"""
if #add_dish_menu is called with an instance of DishCreator
#display_menu will return a list containing that dish
"""
def test_add_one_dish_display_menu():
    dish1 = DishCreator("Pizza", "2.00")
    menu = MenuCreator()
    menu.add_dish_menu(dish1)
    assert menu.display_menu() == [dish1]

"""
if #add_dish is called with 2 instances of DishCreator
#display_menu will return a list containing both dishes,
"""
@pytest.mark.skip(reason="Not yet implemented")
def test_add_two_dishes_display_menu():
    dish1 = DishCreator("Pizza", "2.00")
    dish2 = DishCreator("Pasta", "3.00")
    menu = MenuCreator()
    menu.add_dish_menu(dish1)
    menu.add_dish_menu(dish2)
    assert menu.display_menu() == [dish1, dish2]