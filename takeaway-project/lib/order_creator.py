# File: lib/order_creator.py
#from dish_creator import DishCreator
#from menu_creator import MenuCreator

class OrderCreator():
    def __init__(self, menu):
        self.menu = menu.display_menu()
        self.order = {}

    def add_to_order(self, dish, quantity):
        if not dish in self.menu:
            raise Exception("Dish is not on the menu.")

        if dish in self.order:
            self.order[dish]['Quantity'] += quantity
            self.order[dish]['Price'] = self.menu[dish] * self.order[dish]['Quantity']
        else:
            self.order[dish] = {"Quantity": quantity, "Price": (self.menu[dish] * quantity)}

    def remove_from_order(self, dish):
        if not dish in self.order:
            raise Exception("Dish not in basket.")

        del self.order[dish]

    def clear_order(self):
        if self.order == {}:
            raise Exception('Basket is already empty.')

        self.order = {}

    def itemised_total(self):
        if self.order == {}:
            return 'Basket is empty.'

        order_total = 0
        items = []

        for dish in self.order:
            quantity = self.order[dish]['Quantity']
            price_quant = self.order[dish]['Price']
            order_total += price_quant
            items.append(f'{quantity} {dish} - {price_quant:.2f}')
        
        items_str = ', '.join(items)
        order_total_str = f'Order Total: £{order_total:.2f}'
        
        return f'Dishes: {items_str}\n{order_total_str}'

        #dish = 'Pizza'
        #quantity = self.order['Pizza']['Quantity']
        #price = (self.order['Pizza']['Price'])
        #return f'Dishes: {quantity} {dish} - {price:.#2f}  Order Total: {price:.2f}'


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