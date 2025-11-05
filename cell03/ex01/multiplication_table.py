try:
    print("Enter a number")
    number_input = input()
    N = int(number_input) 
    for i in range(10): 
        result = i * N
        print(f"{i} x {N} = {result}")
except ValueError:
    pass
except EOFError:
    pass