# Fahrenheit °F to Celsius °C Formula
import math

fahrenheit = int(input('Tempature in fahrenheit: '))

celsius = (fahrenheit - 32) / 1.8

print(fahrenheit,'°F to celsius is',format(celsius,".2f"),'°C')