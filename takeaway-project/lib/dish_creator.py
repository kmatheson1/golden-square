# File: lib/dish_creator.py

class DishCreator():
    def __init__(self, dish, price):
        self.dish = dish
        self.price = float(price)
        self.available = True

        if self.dish == "":
            raise Exception("Dish must have a name.")

        if self.price <= 0.00:
            raise Exception("Dish must have a cost.")

    def mark_unavailable(self):
        #makes dish unavailable to be used on an ordering menu
        if not self.available:
            raise Exception("Dish already unavailable.")
        
        self.available = False

    def mark_available(self):
        #makes dish available to be used on an ordering menu
        if self.available:
            raise Exception("Dish already available.")

        self.available = True