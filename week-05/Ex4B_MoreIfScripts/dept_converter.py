# Write a script named dept_converter.py that uses if/elif/else logic to determine
# and print department name based on a department code. Make sure to test your 
# script with multiple codes

dep_code = int(input('What is your department code: '))

if dep_code == 1:
    print('You are in the Marketing Department')
elif dep_code == 5:
    print('You are in the Human Resources Department')
elif dep_code == 10:
    print('You are in the Accounting Department')
elif dep_code == 12:
    print('You are in the Legal Department')
elif dep_code == 18:
    print('You are in the IT Department')
elif dep_code == 20:
    print('You are in the Customer Relations Department')
else:
    print('Your department code is invaild')