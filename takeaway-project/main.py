# File: main.py

from lib.dish_creator import DishCreator
from lib.menu_creator import MenuCreator
from lib.order_creator import OrderCreator
from lib.order_sender import OrderSender
from lib.text_sender import TextSender

#Create your dishes
dish1 = DishCreator("Pizza", "2.00")
dish2 = DishCreator("Pasta", "3.00")
dish3 = DishCreator("Steak", "4.00")
dish4 = DishCreator("Tuna", "4.00")
dish5 = DishCreator("Bread", "1.00")
print('Dishes Created.')

#Add your dishes to the menu
menu = MenuCreator()
menu.add_dish_menu(dish1)
menu.add_dish_menu(dish2)
menu.add_dish_menu(dish3)
menu.add_dish_menu(dish4)
menu.add_dish_menu(dish5)
print('Dishes Added to Menu.\n\n')

#Starts Ordering Program
order = OrderCreator(menu)
print('Please Create your order from the following menu:')
print(order.display_formatted_menu())

#Main Order Creator
def main():
    while True:
        print("\n1. Add to order")
        print("2. Remove from order")
        print("3. Clear")
        print("4. View Order")
        print("5. Send Order")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_to_order(order)

        elif choice == "2":
            remove_from_order(order)

        elif choice == "3":
            try:
                order.clear_order()
                print('Order cleared.')
            except Exception:
                print('Order is already empty.')

        elif choice == "4":
            print(f'\n{order.itemised_total()}')

        elif choice == "5":
            send_order(order)
            break        

        elif choice == "6":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

#Add to order feature
def add_to_order(order):
    while True:
        try:
            dish_name = input("\nEnter dish name to add to the order (or 'done' to finish): ").lower().capitalize()
            if dish_name.lower() == "done":
                break

            while True:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity cannot be 0 or negative. Please enter a valid quantity.")
                else:
                    order.add_to_order(dish_name, quantity)
                    print(f"{quantity} {dish_name}(s) added to the order.")
                    break

        except Exception:
            print("\nDish is not on the Menu.")

#Remove from order feature
def remove_from_order(order):
    while True:
        try:
            dish_name = input("\nEnter dish name to remove from the order (or 'done' to finish): ").lower().capitalize()
            if dish_name.lower() == "done":
                break
            order.remove_from_order(dish_name)
            print(f"{dish_name} removed from the order.")
        except Exception:
            print('\nDish not in Basket.')

#send order feature 
def send_order(order):
    if order.itemised_total() == 'Basket is empty.':
            print('\nNo order to send.\n')
    else:
        sent_order = OrderSender(order)
        print("\nOrder Sent.\n")
            
    while True:
        print("\n1. View Recipt ")
        print("2. View Time Order Sent ")
        print("3. View ETA")
        print("4. Receive Confirmation as text message")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            print(f'\n{sent_order.view_receipt()}')

        elif choice == "2":
            print(f'\n{sent_order.time_sent()}')

        elif choice == "3":
            print(f'\n{sent_order.format_eta()}')

        elif choice == "4":
            user_number = input("\nPlease enter your UK phone number: ")
            text = TextSender(sent_order, user_number)
            print('\nMessage sent.')
            text.send_text()

        elif choice == "5":
            print("Exiting the program.")
            break

if __name__ == "__main__":
    main()


