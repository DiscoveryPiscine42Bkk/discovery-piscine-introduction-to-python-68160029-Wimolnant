try:
    user_input = input("Give me a word: ")
    uppercase_output = user_input.upper()
    print(uppercase_output)
except EOFError:
    pass
except Exception:
    pass