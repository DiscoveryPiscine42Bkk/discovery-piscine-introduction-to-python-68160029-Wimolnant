try:
    user_input = input() 
    swapped_output = user_input.swapcase()
    print(swapped_output)
except EOFError:
    pass
except Exception:
    pass