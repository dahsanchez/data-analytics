import random 
import math 
import statistics

vals_1_100 = range(1,100) 
vals_sample = random.sample(vals_1_100, 75) 
vals_choices = random.choices(vals_1_100, k = 200)  
radius = random.randint(3,10)  
pi = math.pi 

print(f"Sample of 75 values from 1 to 100: {vals_sample}")
