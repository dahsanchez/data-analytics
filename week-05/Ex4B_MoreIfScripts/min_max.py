# displays both the smallest and then the 
# largest of three numbers.

a = 23
b = 5
c = 150

if a <= b and a <= c:
    smallest = a
elif b <= a and b <= c:
    smallest = b
else:
    smallest = c

print(smallest)

if a >= b and a >= c:
    biggest = a
elif b >= a and b >= c:
    biggest = b
else:
    biggest = c 

print(f'The smallest number is {smallest} ')
print(f'The biggest number is {biggest}')