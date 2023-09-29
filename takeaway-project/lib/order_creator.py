# File: lib/order_creator.py
#from dish_creator import DishCreator
#from menu_creator import MenuCreator

class OrderCreator():
    def __init__(self, menu):
        #initialized with menu in dictionary form and empty order dictionary

        if menu == []:
            raise Exception("Menu is empty.")

        self._menu = menu.display_menu()
        self._order = {}

    def display_formatted_menu(self):
        #user can call a formatted version of the menu they can order from.
        return "Dishes  Prices\n" + "\n".join([f'{key}  £{value:.2f}' for key, value in self._menu.items()])

    def add_to_order(self, dish, quantity):
        if not dish in self._menu:
            raise Exception("Dish is not on the menu.")
        
        #adds quantity and totalprice of dishes to ordeorder dictionary.  If dish is already on the _order, the quantity/total price will be updated.
        if dish in self._order:
            self._order[dish]['Quantity'] += quantity
            self._order[dish]['Price'] = self._menu[dish] * self._order[dish]['Quantity']
        else:
            self._order[dish] = {"Quantity": quantity, "Price": (self._menu[dish] * quantity)}

    def remove_from_order(self, dish):
        if not dish in self._order:
            raise Exception("Dish not in basket.")

        del self._order[dish]

    def clear_order(self):
        if self._order == {}:
            raise Exception('Basket is already empty.')
        
        self._order = {}

    def itemised_total(self):
        if self._order == {}:
            return 'Basket is empty.'

        order_total = 0
        items = []

        #iterates through _order to add prices to format quantity, dish, prices, and add prices to total.
        for dish in self._order:
            quantity = self._order[dish]['Quantity']
            price_quant = self._order[dish]['Price']
            order_total += price_quant
            items.append(f'{quantity} {dish} - {price_quant:.2f}')
        
        items_str = '\n'.join(items)
        order_total_str = f'Order Total: £{order_total:.2f}'
        
        return f'Dishes:\n{items_str}\n{order_total_str}'


#dish1 = DishCreator("Pizza", "2.00")
#dish2 = DishCreator("Pasta", "3.00")
#dish3 = DishCreator("Steak", "4.00")
#dish4 = DishCreator("Tuna", "4.00")
#dish5 = DishCreator("Garlic Bread", "1.00")
#_menu = MenuCreator()
#_menu.add_dish_menu(dish1)
#_menu.add_dish_menu(dish2)
#_menu.add_dish_menu(dish3)
#_menu.add_dish_menu(dish4)
#order1 = OrderCreator(_menu)
#print(order1._menu)
#order1.add_to_order("Pasta", 1)
#print(order1._order)