from main import Dishes
import json

class Inventory:

    def load_data(self):
        try:
            with open("menu.json", "r") as file:
                data = json.load(file)
                self.dishes = {}
                for category, dish_list in data.items():
                    self.dishes[category] = [Dishes(**dish) for dish in dish_list]
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

    def addDish(self,id,name,price,availability,category):
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
        dish = Dishes(id=id, name=name,price=price,availability=availability,category=category)
        self.dishes[category].append(dish)
        self.save_data()
        print("------------------------------------------------------------------")
        print(f"Dish with id {id} is added to the {category} catogery in the menu")
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
            confirmation = input(f"Are you sure you want to remove dish with ID {id}? (yes/no): ").strip().lower()
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


        while True:
            try:
                id = int(input("Enter the ID of the dish you want to order (or 0 to exit): "))
                if id == 0:
                    print("Order process canceled.")
                    return
                if any(dish.id == id for dishes in self.dishes.values() for dish in dishes):
                    name = input("Enter name of the Customer: ")
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
                        print(f"Added order in the name of {name} for {quantity} units of {selected_dish.name} to the order.")
                        order_total += item_total

                        self.order.append({
                            "customer_name" : name,
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
            for item in self.order:
                print(f"Customer Name: {item['customer_name']}, Dish: {item['name']}, Quantity: {item['quantity']}, Total: ${item['total']}")
            print(f"Order Total: ${order_total}")
            print("------------------------------------------------")

    def get_all_orders(self):
        self.load_orders()
        if not self.order:
            print("No orders found.")
            return
        print("------------------------------------------------")
        print("All Orders:")
        for index, order_item in enumerate(self.order, start=1):
            print(f"Order {index}:")
            print(f"Customer Name: {order_item['customer_name']}")
            print(f"Dish: {order_item['name']}")
            print(f"Quantity: {order_item['quantity']}")
            print(f"Total: ${order_item['total']}")
            print("--------------------------------------------")
        print("------------------------------------------------")



