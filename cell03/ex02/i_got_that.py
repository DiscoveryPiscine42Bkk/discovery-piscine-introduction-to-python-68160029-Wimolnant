user_input = "" 
print("What you gotta say?")
while True:
    try:
        user_input = input()
        if user_input == "STOP":
            break
        print("I got that! Anything else?:")
    except EOFError:
        break
    except Exception:
        break