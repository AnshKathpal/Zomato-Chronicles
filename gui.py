import tkinter as tk
from tkinter import ttk
from inventory import Inventory


class RestaurantApp:
    def __init__(self, root):
        self.inventory = Inventory()
        self.root = root
        self.root.title("Zomato Chronicles")
        self.orders = []

        # Grid
        self.grid = ttk.Frame(root)
        self.grid.pack(padx=10, pady=10)
        # Grid

        # Get Menu Section Starts
        self.get_menu_frame = ttk.LabelFrame(
            self.grid, text="Get Menu", padding=(10, 10))
        self.get_menu_frame.grid(
            row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.text_widget = tk.Text(self.get_menu_frame, height=10, width=100)
        self.text_widget.pack()
        menu_button = tk.Button(self.get_menu_frame,
                                text="Get Updated Menu", command=self.display_menu)
        menu_button.pack()
        # Get Menu Section Ends

        # Add Dish Starts
        self.add_dish_frame = ttk.LabelFrame(
            self.grid, text="Add Dish", padding=(10, 10))
        self.add_dish_frame.grid(
            row=0, column=1, padx=10, pady=10, sticky="nsew")

        self.label_id = tk.Label(self.add_dish_frame, text="Dish ID:")
        self.entry_id = tk.Entry(self.add_dish_frame)
        self.label_name = tk.Label(self.add_dish_frame, text="Dish Name:")
        self.entry_name = tk.Entry(self.add_dish_frame)
        self.label_price = tk.Label(self.add_dish_frame, text="Dish Price:")
        self.entry_price = tk.Entry(self.add_dish_frame)
        self.label_availability = tk.Label(
            self.add_dish_frame, text="Availability:")
        self.entry_availability = tk.Entry(self.add_dish_frame)
        self.label_category = tk.Label(self.add_dish_frame, text="Category:")
        self.entry_category = tk.Entry(self.add_dish_frame)

        self.add_button = tk.Button(
            self.add_dish_frame, text="Add Dish", command=self.add_dish)

        self.label_id.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.label_name.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_name.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.label_price.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_price.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.label_availability.grid(
            row=3, column=0, padx=5, pady=5, sticky="w")
        self.entry_availability.grid(
            row=3, column=1, padx=5, pady=5, sticky="w")
        self.label_category.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        self.entry_category.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        self.add_button.grid(row=5, columnspan=2, pady=10)
        # Add Dish Ends

        # Update Availibility Starts
        self.update_availability_frame = ttk.LabelFrame(
            self.grid, text="Update Availability", padding=(10, 10))
        self.update_availability_frame.grid(
            row=0, column=2, padx=10, pady=10, sticky="nsew")

        self.label_update_id = tk.Label(
            self.update_availability_frame, text="Dish ID:")
        self.entry_update_id = tk.Entry(self.update_availability_frame)
        self.label_update_availability = tk.Label(
            self.update_availability_frame, text="Availability:")
        self.entry_update_availability = tk.Entry(
            self.update_availability_frame)
        self.update_button = tk.Button(
            self.update_availability_frame, text="Update Availability", command=self.update_availability)

        self.label_update_id.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_update_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.label_update_availability.grid(
            row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_update_availability.grid(
            row=1, column=1, padx=5, pady=5, sticky="w")
        self.update_button.grid(row=2, columnspan=2, pady=10)
        # Update Availibility Starts

        # Remove Dish Starts
        self.remove_frame = ttk.LabelFrame(
            self.grid, text="Remove Dish", padding=(10, 10))
        self.remove_frame.grid(
            row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.label_remove_id = tk.Label(
            self.remove_frame, text="Dish ID:")
        self.entry_remove_id = tk.Entry(self.remove_frame)
        self.remove_button = tk.Button(
            self.remove_frame, text="Remove Dish", command=self.remove_dish)

        self.label_remove_id.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_remove_id.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.remove_button.grid(row=1, columnspan=2, pady=10)
        # Remove Dish Ends

        # Take Order Starts

        self.order_frame = ttk.LabelFrame(
            self.grid, text="Take Order", padding=(10, 10))
        self.order_frame.grid(
            row=1, column=1, padx=10, pady=10, sticky="nsew")
        # Cust name
        self.label_cust_name = tk.Label(
            self.order_frame, text="Customer Name:"
        )
        self.entry_cust_name = tk.Entry(self.order_frame)
        self.label_order_id = tk.Label(
            self.order_frame, text="Dish ID:")
        self.entry_order_id = tk.Entry(self.order_frame)
        self.label_order_qty = tk.Label(
            self.order_frame, text="Order Quantity:")
        self.entry_order_qty = tk.Entry(self.order_frame)
        self.order_button = tk.Button(
            self.order_frame, text="Take Order",
              command=self.take_order
              )

        self.label_cust_name.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_cust_name.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.label_order_id.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.entry_order_id.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.label_order_qty.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.entry_order_qty.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.order_button.grid(row=3, columnspan=2, pady=10)

        self.current_order_id = 1
        self.current_order_items = []

        # Display Order Starts
        self.display_order_frame = ttk.LabelFrame(
            self.grid, text="Display Order", padding=(10, 10))
        self.display_order_frame.grid(
            row=1, column=2, padx=10, pady=10, sticky="nsew")
        self.order_widget = tk.Text(self.display_order_frame , height=10, width = 60)
        self.order_widget.grid(row=1, column=2, columnspan=3)
        self.order_widget.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        # Display Order Ends

        # Display Order-Details Starts
        self.display_orders_frame = ttk.LabelFrame(
            self.grid, text="Display Orders", padding=(10, 10))
        self.display_orders_frame.grid(
            row=2, column=0, padx=10, pady=10, sticky="nsew")
        
        self.order_text_widget = tk.Text(
            self.display_orders_frame, height=10, width=60)
        self.order_text_widget.grid(
            row=0, column=0, padx=5, pady=5, sticky="w")
        
        filter_label = tk.Label(self.display_orders_frame, text="Filter Orders:")
        filter_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.status_var = tk.StringVar()
        self.status_var.set("All Orders")

        filter_options = ["All Orders", "Received", "Ready for Pickup", "Delivered"]
        filter_dropdown = tk.OptionMenu(
            self.display_orders_frame, self.status_var, *filter_options)
        filter_dropdown.grid(row=1, column=1, padx=5, pady=5, sticky="w")

        filter_button = tk.Button(
            self.display_orders_frame, text="Filter", command=self.filter_orders)
        filter_button.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        # Display Order-Details Ends


        #Update-Orders Starts
        self.update_status_frame = ttk.LabelFrame(
            self.grid, text="Update Order Status", padding=(10, 10))
        self.update_status_frame.grid(
            row=2, column=1, padx=10, pady=10, sticky="nsew")
        self.label_update_order = tk.Label(
            self.update_status_frame, text="Order ID:")
        self.entry_update_status = tk.Entry(self.update_status_frame)
        self.label_update_order.grid(
            row=0, column=0, padx=5, pady=5, sticky="w")
        self.entry_update_status.grid(row=0, column=1, padx=5, pady=5, sticky="w")


        filter_update_label = tk.Label(self.update_status_frame, text="Status:")
        filter_update_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

        self.status_var_update = tk.StringVar()
        self.status_var_update.set("Received")

        filter_options_update = ["Received", "Ready for Pickup", "Delivered"]
        filter_dropdown_update = tk.OptionMenu(
            self.update_status_frame, self.status_var_update, *filter_options_update)
        filter_dropdown_update.grid(row=1, column=1, padx=5, pady=5, sticky="w")


        filter_button_update = tk.Button(
            self.update_status_frame, text="Update Status", command=self.update_order_status)
        filter_button_update.grid(row=2, columnspan=2, padx=5, pady=5, sticky="w")
        #Update-Orders Ends


    def add_dish(self):
        id = int(self.entry_id.get())
        name = self.entry_name.get()
        price = float(self.entry_price.get())
        availability = self.entry_availability.get()
        category = self.entry_category.get()

        self.inventory.addDish(id, name, price, availability, category)

        self.entry_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_availability.delete(0, tk.END)
        self.entry_category.delete(0, tk.END)

    def display_menu(self):
        self.text_widget.delete(1.0, tk.END)

        dish_details = self.inventory.get_all_dishes()
        for dish_detail in dish_details:
            self.text_widget.insert(tk.END, dish_detail + "\n")

    def update_availability(self):
        id = int(self.entry_update_id.get())
        update_availability = self.entry_update_availability.get().capitalize()

        dish_found = False
        for category, dishes in self.inventory.dishes.items():
            for dish in dishes:
                if dish.id == id:
                    dish_found = True
                    dish.update_availability(update_availability)
                    break
        if dish_found:
            print(
                f"Availability for Dish with ID {id} updated to {update_availability}.")
        else:
            print(f"No Dish with ID {id} found in the inventory.")

        self.entry_update_id.delete(0, tk.END)
        self.entry_update_availability.delete(0, tk.END)

    def remove_dish(self):
        id = int(self.entry_remove_id.get())
        dish_to_remove = None
        for category, dishes in self.inventory.dishes.items():
            for dish in dishes:
                if dish.id == id:
                    dish_to_remove = dish
                    break
        if dish_to_remove:
            for category, dishes in self.inventory.dishes.items():
                if dish_to_remove in dishes:
                    dishes.remove(dish_to_remove)
                    break
            print(f"Dish with ID {id} has been removed from the menu.")
        else:
            print(f"No dish with ID {id} found in the menu.")
        self.entry_remove_id.delete(0, tk.END)

    def take_order(self):
        customer_name = self.entry_cust_name.get()
        dish_id = int(self.entry_order_id.get())
        quantity = int(self.entry_order_qty.get())
        order_status = "Received"

        selected_dish = None
        for dishes in self.inventory.dishes.values():
            for dish in dishes:
                if dish.id == dish_id:
                    selected_dish = dish
                    break

        if selected_dish and quantity > 0:
            item_total = selected_dish.price * quantity
            order_items = [{
                "id": selected_dish.id,
                "name": selected_dish.name,
                "quantity": quantity,
                "total": item_total
            }]

            order_id = self.current_order_id
            self.current_order_id += 1

            order = {
                "id": order_id,
                "customer_name": customer_name,
                "items": order_items,
                "status": order_status
            }

            self.orders.append(order)
        else:
            print("Invalid order. Please check the dish ID and quantity.")



        self.entry_cust_name.delete(0, tk.END)
        self.entry_order_id.delete(0, tk.END)
        self.entry_order_qty.delete(0, tk.END)

        self.display_order_details(order)

    def display_order_details(self, order):
        self.order_widget.delete(1.0, tk.END)
        order_total = sum(item["total"] for item in order["items"])
        self.order_widget.insert(tk.END, "Order Details:\n")
        self.order_widget.insert(tk.END, f"Customer Name: {order['customer_name']}\n")
        self.order_widget.insert(tk.END, f"Order ID: {self.current_order_id}\n")
        self.order_widget.insert(tk.END, f"Order Status: {order['status']}\n")
        self.order_widget.insert(tk.END, "Order Items:\n")

        for item in order["items"]:
            self.order_widget.insert(tk.END, f"Dish: {item['name']}, Quantity: {item['quantity']}, Total: ${item['total']}\n")
        self.order_widget.insert(tk.END, f"Order Total: ${order_total}\n")

    
    def filter_orders(self):
        status_filter = self.status_var.get().lower()
        self.order_text_widget.delete(1.0, tk.END)

        if status_filter == "all orders":
            filtered_orders = self.orders
        else:
            filtered_orders = [order for order in self.orders if order['status'].lower() == status_filter]

        if not filtered_orders:
            self.order_text_widget.insert(
                tk.END, f"No {status_filter.capitalize()} orders found.")
            return

        self.order_text_widget.insert(tk.END, "------------------------------------------------\n")
        self.order_text_widget.insert(tk.END, f"{status_filter.capitalize()} Orders:\n")

        for order in filtered_orders:
            self.order_text_widget.insert(tk.END, f"Order ID: {order['id']}\n")
            self.order_text_widget.insert(tk.END, f"Customer Name: {order['customer_name']}\n")
            self.order_text_widget.insert(tk.END, f"Order Status: {order['status']}\n")
            self.order_text_widget.insert(tk.END, "Order Items:\n")

            for item in order['items']:
                self.order_text_widget.insert(tk.END, f"Dish: {item['name']}\n")
                self.order_text_widget.insert(tk.END, f"Quantity: {item['quantity']}\n")
                self.order_text_widget.insert(tk.END, f"Total: ${item['total']}\n")
                self.order_text_widget.insert(tk.END, "--------------------------------------------\n")



    def update_order_status(self):
        order_id = int(self.entry_update_status.get())
        new_status = self.status_var_update.get()

        found = False

        for order in self.orders:
            if order_id == order.get('id'):
                if new_status in ["Received", "Preparing", "Ready for Pickup", "Delivered"]:
                    order['status'] = new_status.lower()
                    print(f"Order with ID {order_id} is now '{new_status}'.")
                    found = True
                    self.filter_orders()
                    break
        if not found:
            print(f"No order found with ID {order_id}.")
            


if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantApp(root)
    root.mainloop()
