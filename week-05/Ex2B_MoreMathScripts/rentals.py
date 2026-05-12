# There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost 
# $250 per day to rent (including the driver’s pay). How many vans do you need? How 
# much will it cost to rent vans? What is the cost if you split it per person?
import math

num_of_ppl = int(input('How many people are going on the tour: '))
num_of_days = int(input('How many days is the tour: '))

camper_van = math.ceil(num_of_ppl / 15)
cost = num_of_days * 250
total_cost = cost * camper_van
cost_per_person = math.ceil(total_cost / num_of_ppl)

print(f"For {num_of_ppl} people you are going to need {camper_van} van/s")
print(f"For {num_of_days} day/s it will cost ${total_cost}")
print(f"Each person will have to pay ${round(cost_per_person,2)}")