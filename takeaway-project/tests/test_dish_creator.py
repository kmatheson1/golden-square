# File: tests/test_dish_creator.py
import pytest
from lib.dish_creator import DishCreator

"""
When instanciated
constrcuts with dish title and availability
"""
def test_dish_creator_construct():
    dish = DishCreator("Pizza", "2.00")
    assert dish.dish == "Pizza"
    assert dish.price == "2.00"
    assert dish.available == True

def test_mark_unavailable_updates_available():
    dish = DishCreator("Pizza", "2.00")
    dish.mark_unavailable()
    assert dish.available == False