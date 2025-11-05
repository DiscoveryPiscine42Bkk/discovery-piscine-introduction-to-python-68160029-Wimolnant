try:
    age_input = input("Please tell me your age: ")
    current_age = int(age_input)
    print(f"You are currently {current_age} years old.")
    age_in_10 = current_age + 10
    print(f"In 10 years, you'll be {age_in_10} years old.")
    age_in_20 = current_age + 20
    print(f"In 20 years, you'll be {age_in_20} years old.")
    age_in_30 = current_age + 30
    print(f"In 30 years, you'll be {age_in_30} years old.")
except ValueError:
    pass
except EOFError:
    pass