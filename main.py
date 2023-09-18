class Dishes:
    def __init__(self,id,name,price,availability,category):
        self.id = id
        self.name = name
        self.price = price
        self.availability = availability
        self.category = category


    def update_availability(self, update_availability):
        self.availability = update_availability

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "availability": self.availability,
            "category": self.category
        }


    def getDetails(self):
        return f"Dishes(Dish_Id = {self.id}, Dish Name = {self.name}, Dish Price = {self.price}, Dish Availability = {self.availability})"
    
    def __str__(self):
        return self.getDetails()
    
