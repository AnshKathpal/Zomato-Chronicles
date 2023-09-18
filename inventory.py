from main import Dishes
import json


class Inventory:

    def load_data(self):
        try:
            with open("menu.json", "r") as file:
                data = json.load(file)
                self.dishes = {}
                for category, dish_list in data.items():
                    self.dishes[category] = [
                        Dishes(**dish) for dish in dish_list]
        except FileNotFoundError:
            self.dishes = {}

    def load_orders(self):
        try:
            with open("orders.json", "r") as file:
                self.order = json.load(file)
        except FileNotFoundError:
            self.order = []

    def save_orders(self):
        with open("orders.json", "w") as file:
            json.dump(self.order, file, indent=4)

    def save_data(self):
        serialized_data = {}
        for category, dishes in self.dishes.items():
            serialized_data[category] = [dish.to_dict() for dish in dishes]
        with open("menu.json", "w") as file:
            json.dump(serialized_data, file, indent=4)

    def __init__(self):
        self.load_data()
        self.load_orders()
        self.order = []

    def addDish(self, id, name, price, availability, category):
        if category not in self.dishes:
            self.dishes[category] = []
        for dish in self.dishes[category]:
            if dish.id == id:
                print("---------------------------------------")
                print(f"Dish is already present with id {id}")
                print("---------------------------------------")
                dish.name = name
                dish.price = price
                dish.availability = availability
                self.save_data()
                return
        dish = Dishes(id=id, name=name, price=price,
                      availability=availability, category=category)
        self.dishes[category].append(dish)
        self.save_data()
        print("------------------------------------------------------------------")
        print(
            f"Dish with id {id} is added to the {category} catogery in the menu")
        print("------------------------------------------------------------------")

    def get_all_dishes(self):
        dish_details = []
        for category, dishes in self.dishes.items():
            for dish in self.dishes[category]:
                dish_details.append(
                    f" Category: {category} -> Id : {dish.id}, Name : {dish.name}, Price : {dish.price}, Availability : {dish.availability}"
                )
        return dish_details

    def remove_Dish(self):
        all_dishes = self.get_all_dishes()
        if not all_dishes:
            print("------------------------------------------------")
            print("No Dishes in the inventory to remove.")
            print("------------------------------------------------")
            return
        print("------------------------------------------------")
        print("Dishes Details")

        for dishdetails in all_dishes:
            print("--------------------------------------------")
            print(dishdetails)
            print("--------------------------------------------")
        id = int(input("Enter Id to remove the dish from the Menu: "))
        dish_to_remove = None
        for category, dishes in self.dishes.items():
            for dish in dishes:
                if dish.id == id:
                    dish_to_remove = dish
                    break
        if dish_to_remove:
            confirmation = input(
                f"Are you sure you want to remove dish with ID {id}? (yes/no): ").strip().lower()
            if confirmation == "yes":
                self.dishes[dish_to_remove.category].remove(dish_to_remove)
                print("------------------------------------------------")
                print(
                    f"Dish with ID {id} has been removed from the menu.")
                print("------------------------------------------------")
                self.save_data()
            else:
                print("------------------------------------------------")
                print("Dish Remove Canceled.")
        else:
            print("------------------------------------------------")
            print(f"No dish with ID {id} found in the menu.")
            print("------------------------------------------------")

    def take_order(self):
        print("------------------------------------------------")
        print("Menu for Taking a New Order")
        all_dishes = self.get_all_dishes()
        for dishdetails in all_dishes:
            print("--------------------------------------------")
            print(dishdetails)
            print("--------------------------------------------")

        order_total = 0
        order_id = len(self.order) + 1

        name = input("Enter name of the Customer: ")
        status = "received"

        order_items = []

        while True:
            try:
                id = int(
                    input("Enter the ID of the dish you want to order (or 0 to exit): "))
                if id == 0:
                    if order_total == 0:
                        print("Order process canceled.")
                    else:
                        self.order.append({
                            "order_id": order_id,
                            "customer_name": name,
                            "status": status,
                            "items": order_items
                        })
                        print(f"Order with ID {order_id} has been placed.")
                        self.save_orders()
                    return
                if any(dish.id == id for dishes in self.dishes.values() for dish in dishes):
                    quantity = int(input("Enter the quantity: "))
                    if quantity < 1:
                        print("Quantity must be greater than 0.")
                    else:
                        selected_dish = None
                        for dishes in self.dishes.values():
                            for dish in dishes:
                                if dish.id == id:
                                    selected_dish = dish
                                    break
                        if selected_dish:
                            item_total = selected_dish.price * quantity
                        print(
                            f"Added order in the name of {name} for {quantity} units of {selected_dish.name} to the order.")
                        order_total += item_total

                        order_items.append({
                            "id": selected_dish.id,
                            "name": selected_dish.name,
                            "quantity": quantity,
                            "total": item_total
                        })
                        self.save_orders()
                else:
                    print("Invalid Dish ID. Please enter a valid ID from the menu.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

            print("------------------------------------------------")
            print("Order Details:")
            print(f"Order ID: {order_id}")
            print(f"Customer Name: {name}")
            print(f"Order Status: {status}")
            for item in order_items:
                print(
                    f"Dish: {item['name']}, Quantity: {item['quantity']}, Total: ${item['total']}")
            print(f"Order Total: ${order_total}")
            print("------------------------------------------------")

    def get_all_orders(self,status_filter=None):
        self.load_orders()
        if not self.order:
            print("No orders found.")
            return
        print("------------------------------------------------")
        print("All Orders:")
        for order_item in self.order:
            if status_filter is None or order_item['status'] == status_filter:
                print(f"Order ID: {order_item['order_id']}")
                print(f"Customer Name: {order_item['customer_name']}")
                print(f"Order Status: {order_item['status']}")
                for item in order_item['items']:
                    dish_id = item['id']
                    dish_name = None
                    for category, dishes in self.dishes.items():
                        for dish in dishes:
                            if dish.id == dish_id:
                                dish_name = dish.name
                                break
                        if dish_name:
                            break
                    print(f"Dish: {dish_name}")
                    print(f"Quantity: {item['quantity']}")
                    print(f"Total: ${item['total']}")
                    print("--------------------------------------------")
        print("------------------------------------------------")

    def update_order_status(self, order_id):
        for order in self.order:
            if order['order_id'] == order_id:
                print("Select the new status:")
                print("1. Preparing")
                print("2. Ready for Pickup")
                print("3. Delivered")
                choice = input("Enter your choice (1/2/3): ")
                if choice == "1":
                    order['status'] = 'preparing'
                    print(f"Order with ID {order_id} is now 'preparing'.")
                elif choice == "2":
                    order['status'] = 'ready for pickup'
                    print(
                        f"Order with ID {order_id} is now 'ready for pickup'.")
                elif choice == "3":
                    order['status'] = 'delivered'
                    print(f"Order with ID {order_id} is now 'delivered'.")
                else:
                    print("Invalid choice. Order status remains unchanged.")
                self.save_orders()
                return
            print(f"No order found with ID {order_id}.")
