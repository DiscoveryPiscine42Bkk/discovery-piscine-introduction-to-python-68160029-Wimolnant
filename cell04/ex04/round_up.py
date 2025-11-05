import math
try:
    user_input = input("Give me a number: ")
    number_float = float(user_input)
    rounded_up_float = math.ceil(number_float)
    rounded_up_integer = int(rounded_up_float)
    print(rounded_up_integer)
except ValueError:
    pass
except EOFError:
    pass