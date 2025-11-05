try:
    user_input = input("Give me a number: ")
    number_float = float(user_input)
    if number_float.is_integer():
        print("This number is an integer.")
    else:
        print("This number is a decimal.")
except ValueError:
    pass
except EOFError:
    pass