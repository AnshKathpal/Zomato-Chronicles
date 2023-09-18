from inventory import Inventory

inventory = Inventory()

while True:
    print("+------------------------+")
    print("+       Operations       +")
    print("+------------------------+")
    print("+ 1. Add Dishes          +")
    print("+------------------------+")
    print("+ 2. View Menu           +")
    print("+------------------------+")
    print("+ 3. Update Availbility  +")
    print("+------------------------+")
    print("+ 4. Remove Dish         +")
    print("+------------------------+")
    print("+ 5. Exit                +")
    print("+------------------------+")

    choice = input("Select an option (1/2/3/4/5): ")

    if choice == "1":
        id = int(input("Enter Dish Id: "))
        name = input("Enter dish name: ")
        price = float(input("Enter dish price: "))
        availability = input("Is Available (Yes/No): ")
        category = input("Choose Category (Breakfast/Lunch/Dinner/All Day): ")
        inventory.addDish(id, name, price, availability, category)
    elif choice == "2":
        all_dishes = inventory.get_all_dishes()
        for dishdetails in all_dishes:
            print("--------------------------------------------")
            print(dishdetails)
            print("--------------------------------------------")
    elif choice == "3":
        all_dishes = inventory.get_all_dishes()
        for dishdetails in all_dishes:
            print("--------------------------------------------")
            print(dishdetails)
            print("--------------------------------------------")
        id = int(input("Enter Dish Id to Update: "))
        update_availability = input(
            "Enter Updated Availability(Yes/No): ").capitalize()
        dish_Found = False
        for catagory, dishes in inventory.dishes.items():
            for dish in dishes:
                print(f"Searching for Dish ID: {id}")
                print(f"Current Dish ID: {dish.id}")
                if dish.id == id:
                    dish_Found = True
                    dish.update_availability(update_availability)
                    print("--------------------------------------------")
                    print(
                        f"Availability for Dish with ID {id} updated to {update_availability}.")
                    print("--------------------------------------------")
                    break
            if dish_Found:
                break
        if not dish_Found:
            print(
                "--------------------------------------------")
            print(
                f"No Dish with ID {id} found in the inventory.")
            print(
                "--------------------------------------------")
    elif choice == "4":
        inventory.remove_Dish()
    elif choice == "5":
        print("Exiting the application.")
        inventory.save_data()
        break
    else:
        print("Invalid Choice! Please choose the correct option.")