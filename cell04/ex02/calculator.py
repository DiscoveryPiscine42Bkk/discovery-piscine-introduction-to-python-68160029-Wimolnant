try:
    num1_input = input("Give me the first number: ")
    num1 = int(num1_input) 
    num2_input = input("Give me the second number: ")
    num2 = int(num2_input) 
    print("Thank you!")
    addition_result = num1 + num2
    print(f"{num1}+{num2}={addition_result}")
    subtraction_result = num1 - num2
    print(f"{num1}-{num2}={subtraction_result}")
    division_result = num1 / num2
    if num1 % num2 == 0:
        print(f"{num1}/{num2}={int(division_result)}")
    else:
        print(f"{num1}/{num2}={division_result}")
    multiplication_result = num1 * num2
    print(f"{num1}*{num2}={multiplication_result}")
except ValueError:
   pass
except ZeroDivisionError:
    print(f"{num1}/{num2}=Cannot divide by zero")
except EOFError:
    pass