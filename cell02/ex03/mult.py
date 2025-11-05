try:
    print("Enter the first number:")
    num1_input = input()
    num1 = int(num1_input)
    print("Enter the second number:")
    num2_input = input()
    num2 = int(num2_input)
    result = num1 * num2
    
    sign_message = ""
    if result > 0:
        sign_message = "The result is positive."
    elif result < 0:
        sign_message = "The result is negative."
    else: 
        sign_message = "The result is positive and negative." 
    print(f"{num1} x {num2} = {result}")
    print(sign_message)
except ValueError:
    pass
except EOFError:
    pass