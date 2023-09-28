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
def test_itemised_total_for_one_dish():
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
    assert order1.itemised_total() == "Dishes: 1 Pizza - 3.00\nOrder Total: £3.00"

"""
If #add_dish_menu multiple dish to order
#itemised_total returns each dish price and total price
"""
def test_itemised_total_for_multiple_dish():
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
    order1.add_to_order("Steak", 3)
    assert order1.itemised_total() == "Dishes: 1 Pizza - 3.00, 2 Pasta - 6.00, 3 Steak - 12.00\nOrder Total: £21.00"

"""
If #remove_from_order is called
Whole quantity of that dish is removed from order
"""
def test_remove_from_order_removes_dish():
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
    order1.add_to_order("Steak", 3)
    order1.remove_from_order("Steak")
    assert order1.itemised_total() == "Dishes: 1 Pizza - 3.00, 2 Pasta - 6.00\nOrder Total: £9.00"

"""
If #clear_order is called
Entire order is emptied - returns message
"""
def test_clear_order_and_message():
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
    order1.add_to_order("Steak", 3)
    order1.clear_order()
    assert order1.itemised_total() == "Basket is empty."


