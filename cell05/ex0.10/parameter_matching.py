import sys
if len(sys.argv) != 2:
    print("none")
else:
    expected_parameter = sys.argv[1]
    user_word = input("What was the parameter? ")
    if user_word == expected_parameter:
        print("Good job!")
    else:
        print("Nope, sorry...")
