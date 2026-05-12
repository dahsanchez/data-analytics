# Define known values
# using f string
food_cost = 79.25
tax = 6.54
tip = 12.00
# Calculate the unknown
total_due = food_cost + tax + tip
# Display the results
#print("The total due is " + str(total_due))

print(f"Food cost is {food_cost} and tax is {tax}")
#print("Tip is " + str(tip))
print("Tip is " + format(tip, ".2f"))
print(f"Total due is {total_due}")
