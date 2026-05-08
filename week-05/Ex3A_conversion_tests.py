# Description: This script tests various numeric 
#              conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

# a) Cast as integer using int()
# print(int(a)) ValueError: invalid literal for int() with base 10: ' 101.1 '
print(int(b))
# print(int(c)) ValueError: invalid literal for int() with base 10: '402 Stevens'
# print(int(d)) ValueError: invalid literal for int() with base 10: 'Number 5 '

# b) Cast as float using float()
print(float(a))
print(float(b))
# print(float(c)) ValueError: could not convert string to float: '402 Stevens'
# print(float(d)) ValueError: could not convert string to float: 'Number 5 '

# c) For variable a, try casting into a float then integer, like this: int(float(a))
print(int(float(a))) #produces 101 

# d) Use slicing to add just the numeric portion of the string to a new variable
# (remember, indexing always starts with 0!), and cast the number as an integer or 
# string, whichever is appropriate

c_num = int(c[:3])
d_num = int(d[-2])
print(c_num)
print(d_num)

# e) For variables a and d, use the .strip() method to remove the leading/trailing 
# spaces, within a print statement to display each result.

print(a.strip())
print(d.strip())