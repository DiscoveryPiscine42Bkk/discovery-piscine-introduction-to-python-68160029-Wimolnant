user_input = input()
CORRECT_PASSWORD = "Python is awesome"
try:
    if user_input == CORRECT_PASSWORD:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED.")
except EOFError:
    pass
except Exception:
    pass