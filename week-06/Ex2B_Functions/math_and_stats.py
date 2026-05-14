import random 
import math 
import statistics

vals_1_100 = range(1,100) 
vals_sample = random.sample(vals_1_100, 75) 
vals_choices = random.choices(vals_1_100, k = 200)  
radius = random.randint(3,10)  
pi = math.pi 

# Experimenting with a subset of integers 1-100:
# Sum of 75 sample values from 1 to 100: 
sum75 = sum(vals_sample)
# Average of 75 sample values: 
avg75 = sum(vals_sample)/75
# Median of 75 sample values: 
med75 = statistics.median(vals_sample)

# Experimenting with a superset of 200 values, integers 1-100:
# Average of 200 values:
avg200 = sum(vals_choices)/200
# Median of 200 values: 
med200 = statistics.median(vals_choices)
# Mode of 200 values: 
mode200 = statistics.mode(vals_choices)
# Standard deviation of 200 values:
standev200 = statistics.stdev(vals_choices)
# Variance of 200 values:
vari200 = statistics.variance(vals_choices)

# Modeling a random circle:
# Radius = __, area = ____ (rounded up to the nearest integer)
area =  math.ceil(pi * (pow(radius,2)))
# Radius = __, area = ____ (rounded down to the nearest integer)
area2 =  math.floor(pi * (pow(radius,2)))

print(f'''\n_Experimenting with a subset of integers 1-100:
Sum of 75 sample values from 1 to 100: {sum75}
Average of 75 sample values: {avg75}
Median of 75 sample values: {med75}\n
_Experimenting with a superset of 200 values, integers 1-100:
Average of 200 values: {avg200}
Median of 200 values: {med200}
Mode of 200 values: {mode200}
Standard deviation of 200 values: {standev200}
Variance of 200 values: {vari200}\n
_Modeling a random circle:
Radius = {radius}, area = {area} (rounded up to the nearest integer)
Radius = {radius}, area = {area2} (rounded down to the nearest integer)''')
