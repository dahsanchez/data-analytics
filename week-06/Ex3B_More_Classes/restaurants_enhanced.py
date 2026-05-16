class Restaurant:
    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self):
        try:
            count = int(input(f"How many customers served today at {self.rest_name}? "))
            if count < 0:
                print("Please enter a non-negative number.")
                return
            self.number_served += count
        except ValueError:
            print("Please enter a whole number.")

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers.")

    def customer_rating(self):
        try:
            rating = int(input(
                f"How would you rate your experience at {self.rest_name} (1-5)? "))
            if rating < 1 or rating > 5:
                print("Rating must be an integer between 1 and 5.")
                return
            self.customer_ratings.append(rating)
            avg = sum(self.customer_ratings) / len(self.customer_ratings)
            print(f"Your rating was {rating}. The average rating for this restaurant is {avg:.2f}.")
        except ValueError:
            print("Please enter a whole number between 1 and 5.")


rest1 = Restaurant("Weedy's Burger", "burgers and fries")
rest2 = Restaurant("Tinkle Taco", "tacos and burritos")
rest3 = Restaurant("Dunkin Dunnuts", "coffee and donuts")

for r in (rest1, rest2, rest3):
    r.print_num_served()
    r.add_num_served()
    r.add_num_served()
    r.print_num_served()
    r.customer_rating()
    r.customer_rating()