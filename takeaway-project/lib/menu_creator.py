# File: lib/menu_creator.py
#from dish_creator import DishCreator

class MenuCreator():
    def __init__(self):
        self._menu = []

    def add_dish_menu(self, dish):
        self._menu.append(dish)

    def remove_dish(self, dish):
        self._menu.remove(dish)

    def display_menu(self):
        #creates menu as a dictionary
        return {dish.dish: dish.price for dish in self._menu if dish.available}



#dish1 = DishCreator("Pizza", "2.00")
#dish2 = DishCreator("Pasta", "3.00")
#menu = MenuCreator()
#menu.add_dish_menu(dish1)
#menu.add_dish_menu(dish2)
#print(menu.display_menu())