# File: lib/dish_creator.py

class DishCreator():
        def __init__(self, dish, price):
        #   Parameters:
        #       A dish name as a string, a price as a float
        #   Side-effects:
        #       Available property constructed as equal to True
            self.dish = dish
            self.price = price

        def mark_unavailable(self):
        #   Side-effects:
        #       Sets Available property to False
            pass