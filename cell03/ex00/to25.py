print("Enter a number less than 25")
number_input = input()
current_number = int(number_input) 
try:
    if current_number > 25:
        print("Error")
    else:
        while current_number <= 25:
            print(f"Inside the loop, my variable is {current_number}")
            current_number += 1 
except ValueError:
    pass
except EOFError:
    pass