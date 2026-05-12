# how long it would take an invesment to double
import math
invest = 5000
interest_rate = 0.06

years_to_double = 72 / (interest_rate * 100)
new_invest = invest * 2
print('Your current savings is',invest)
print('At a',format(interest_rate,".0%"),'interest rate, your savings account will be worth',format(new_invest,".2f"),'in',format(years_to_double,".1f"))