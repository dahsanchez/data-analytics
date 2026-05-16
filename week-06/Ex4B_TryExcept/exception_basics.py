# Module 4 – Exceptions Lab

# ValueError
try:
    y = float("not_a_number")   # also invalid
except ValueError:
    print("ValueError: Tried converting an invalid string to a float.")
else:
    print(y)
finally:
    print("Let's try another one...\n")

# NameError
try:
    m = banana # undefined variable
except NameError:
    print("NameError: You tried to use a variable that doesn't exist.")
else:
    print(m)
finally:
    print("Let's try another one...\n")

# TypeError
try:
    result = "hello" + 5 # cannot add string + int
except TypeError:
    print("TypeError: Tried adding a string and an integer.")
else:
    print(result)
finally:
    print("Let's try another one...\n")

# SyntaxError 
try:
    eval("5 +") # incomplete expression
except SyntaxError:
    print("SyntaxError: Incomplete or invalid Python expression.")
else:
    print("Expression evaluated successfully.")
finally:
    print("Let's try another one...\n")
