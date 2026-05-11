# Define a variable that contains the current hour (0-
# 23). Display one of the greetings below based on the current hour

current_hour = int(input('What time is it right now(use 24 clock cycle): '))

if 4 < current_hour < 10:
    print('Good morning!')
elif 10 < current_hour < 17:
    print('Good day!')
else:
    print('Good evening!')

if current_hour >= 23 or current_hour < 4:
    print('What are you doing up so late??')