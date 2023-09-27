# File: lib/order_creator.py
#from dish_creator import DishCreator
#from menu_creator import MenuCreator

class OrderCreator():
    def __init__(self, menu):
        self.menu = menu.display_menu()
        self.order = {

        }

    def add_to_order(self, dish, quantity):
        if dish in self.order:
            self.order[dish]['Quantity'] += quantity
        else:
            self.order[dish] = {"Quantity": quantity, "Price": self.menu[dish]}

    def remove_from_order(self, dish):
    #   Parameters:
    #       A dish from the menu
    #   Side-effects:
    #       The dish (all quntity) is removed frothe current order
        pass

    def clear_order(self):
    #   Side-effects:
    #       All dishes removed from current order
        pass

    def itemised_total(self):
    #   Returns:
    #       List of current dishes added to ordertheir prices, and total cost of order so far
        pass


#dish1 = DishCreator("Pizza", "2.00")
#dish2 = DishCreator("Pasta", "3.00")
#dish3 = DishCreator("Steak", "4.00")
#dish4 = DishCreator("Tuna", "4.00")
#dish5 = DishCreator("Garlic Bread", "1.00")
#menu = MenuCreator()
#menu.add_dish_menu(dish1)
#menu.add_dish_menu(dish2)
#menu.add_dish_menu(dish3)
#menu.add_dish_menu(dish4)
#order1 = OrderCreator(menu)
#print(order1.menu)
#order1.add_to_order("Pasta", 1)
#print(order1.order)