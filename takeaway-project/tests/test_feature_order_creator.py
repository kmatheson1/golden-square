# File: tests/test_feature_order_creator.py
from lib.order_creator import OrderCreator
from lib.dish_creator import DishCreator
from lib.menu_creator import MenuCreator
import pytest

"""
When CreateOrder is instanciated
It is constructed with menu as dictionary
"""
def test_create_order_constructed_with_display_menu():
    menu = MenuCreator()
    order1 = OrderCreator(menu)
    assert order1.menu == menu.display_menu()

"""
If add_dish_menu one dish to order
#itemised_total returns dish price and total price
"""
@pytest.mark.skip
def test_itemised_total_for_one_dish():
    dish1 = DishCreator("Pizza", 2.00)
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
    assert order1.itemised_total() == "Dishes: 1 Pizza - 3.00  Order Total: 3.00 "
