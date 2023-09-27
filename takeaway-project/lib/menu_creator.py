# File: lib/menu_creator.py

class MenuCreator():
    def __init__(self):
        self._menu = []

    def add_dish_menu(self, dish):
    #   Parameters:
    #       An instance of the Dish class
    #   Side-effects:
    #       Dish is added to menu dictionary.
        self._menu.append(dish)

    def remove_dish(self, dish):
    #   Parameters:
    #       An instance of the Dish class
    #   Side-effects:
    #       Dish is removed from the menu dictionary.
        pass

    def display_menu(self):
    #   Returns:
    #       Menu in List or dictionary form
        return self._menu 