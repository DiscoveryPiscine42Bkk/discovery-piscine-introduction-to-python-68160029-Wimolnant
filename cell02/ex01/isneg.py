number_input = input()
number = int(number_input)
try: 
    if number < 0:
        print("This number is negative.") 
    elif number > 0:
        print("This number is positive.") 
    else: 
        print("This number is both positive and negative.") 
except ValueError:
    pass