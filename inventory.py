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

    def save_data(self):
        serialized_data = {}
        for category, dishes in self.dishes.items():
            serialized_data[category] = [dish.to_dict() for dish in dishes]
        with open("menu.json", "w") as file:
            json.dump(serialized_data, file, indent=4)

    def __init__(self):
        self.load_data()

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

        