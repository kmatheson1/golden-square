# File: tests/test_dish_creator.py
import pytest
from lib.dish_creator import DishCreator

"""
When instanciated
constrcuts with dish title and availability
"""
def test_dish_creator_construct():
    dish = DishCreator("Pizza", 2.00)
    assert dish.dish == "Pizza"
    assert dish.price == 2.00
    assert dish.available == True

def test_mark_unavailable_updates_available():
    dish = DishCreator("Pizza", 2.00)
    dish.mark_unavailable()
    assert dish.available == False

def test_mark_available_again_updates_availabile():
    dish = DishCreator("Pizza", 2.00)
    dish.mark_unavailable()
    dish.mark_available()
    assert dish.available == True

def test_error_if_empty_string_for_dish():
    with pytest.raises(Exception) as err:
        DishCreator("", 2.00)
    assert str(err.value) == "Dish must have a name."

def test_error_if_price_less_or_equal_zero():
    with pytest.raises(Exception) as err:
        DishCreator("Pizza", 0.00)
    assert str(err.value) == "Dish must have a cost."

def test_error_if_available_on_available():
    dish = DishCreator("Pizza", 2.00)
    with pytest.raises(Exception) as err:
        dish.mark_available()
    assert str(err.value) == "Dish already available."

def test_error_if_unavailable_on_unavailable():
    dish = DishCreator("Pizza", 2.00)
    dish.mark_unavailable()
    with pytest.raises(Exception) as err:
        dish.mark_unavailable()
    assert str(err.value) == "Dish already unavailable."