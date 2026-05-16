
#Exercise 3.A - Working with classes


class Restaurant:
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        
    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")
    def rest_open(self):
        print(f"{self.rest_name} is open.")


rest1 = Restaurant("Weedy's Burger", "burgers and fries")
rest2 = Restaurant("Tinkle Taco", "tacos and burritos")
rest3 = Restaurant("Dunkin Dunnuts", "coffee and donuts")

for r in (rest1, rest2, rest3):
    r.describe_rest()
    r.rest_open()



